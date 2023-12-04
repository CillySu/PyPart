import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import numpy as np

# Read the CSV file into a DataFrame
# Rename partogram_data to your data in csv format.
csvfile = 'partogram_data_KO'
data = pd.read_csv(f'{csvfile}.csv')


# Convert the 'Time' column to datetime
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M')

# Set font settings for the plot
plt.rcParams.update({'font.family': 'Helvetica', 'font.size': 10})


# Create the figure and subplots with different heights
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 10), sharex=True, gridspec_kw={'height_ratios': [1, 1]})


# Top Subplot: Maternal and Fetal Vital Signs
FetalHeartRateMask = np.isfinite(data['FetalHeartRate'])

ax1.plot(data['Time'][FetalHeartRateMask], data['FetalHeartRate'][FetalHeartRateMask], 'x-', label='Fetal Heart Rate', color='black', linewidth=1, alpha=0.7)

ax1.plot(data['Time'], data['MaternalHeartRate'], '.--', label='Maternal Heart Rate', color='black', linewidth=1, alpha=0.7)
ax1.plot(data['Time'], data['MaternalSystolic'], '^', label='Maternal SBP', color='black', markersize=8)
ax1.plot(data['Time'], data['MaternalDiastolic'], 'v', label='Maternal DBP', color='black', markersize=8)
# Connect systolic and diastolic blood pressure points with dashed lines
for i in range(len(data['Time'])):
    ax1.plot([data['Time'][i], data['Time'][i]], [data['MaternalSystolic'][i], data['MaternalDiastolic'][i]], 'k--', linewidth=1, alpha=0.7)



# Customizing the first subplot
ax1.set_ylabel('Heart Rate (bpm) / Blood Pressure (mmHg)')
ax1.set_title('Maternal and Fetal Vital Signs')
ax1.set_ylim(40, 170)
ax1.set_yticks(np.arange(40, 171, 10))
#ax1.legend(loc='lower right')
ax1.grid(True, linestyle=':', linewidth='0.5', color='black')
# Bottom Subplot: Cervical Dilation Progress
data['CervicalDilationInterpolated'] = data['CervicalDilation'].interpolate()
ax2.plot(data['Time'], data['CervicalDilationInterpolated'], '--', color='black', linewidth=1, alpha=0.7)
ax2.plot(data['Time'], data['CervicalDilation'], '*--', label='Cervical Dilation', color='black', linewidth=1, alpha=0.7)

# Adding modified alert and action lines
start_time = data['Time'].min()
end_time = data['Time'].max()
max_cervical_dilation = data['CervicalDilation'].max()

# Calculate the x and y range of the plot
x_range_hours = (end_time - start_time).total_seconds() / 3600
y_range = max_cervical_dilation - 4  # Assuming 4 cm as the starting point for both lines

# Ensure both ranges are equal for 45-degree lines
max_range = max(x_range_hours, y_range)

# Calculate the end points for both lines
alert_line_start = (start_time, 4)
alert_line_end = (start_time + timedelta(hours=max_range), 4 + max_range)

action_line_start = (start_time, 0)
action_line_end = (action_line_start[0] + timedelta(hours=max_range), max_range)

# Plotting the alert and action lines in black
ax2.plot([alert_line_start[0], alert_line_end[0]], [alert_line_start[1], alert_line_end[1]],
         '-', color='black', linewidth=1, label='Alert Line')
ax2.plot([action_line_start[0], action_line_end[0]], [action_line_start[1], action_line_end[1]],
         '-', color='black', linewidth=1, label='Action Line')


# Customizing the second subplot
ax2.set_xlabel('Time')
ax2.set_ylabel('Cervical Dilation (cm)')
ax2.set_title('Cervical Dilation Progress')
ax2.set_ylim(0, max_cervical_dilation)
ax2.set_yticks(np.arange(0, max_cervical_dilation + 1, 1))
ax2.grid(True, linestyle=':', linewidth='0.5', color='black')
#ax2.legend(loc='lower right')

# Setting x-axis format
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax1.xaxis.set_minor_locator(mdates.MinuteLocator(byminute=[15, 30, 45]))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax2.xaxis.set_minor_locator(mdates.MinuteLocator(byminute=[15, 30, 45]))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Adjusting x-axis limits to accommodate the 45-degree lines
ax1.set_xlim(start_time, action_line_end[0])
ax2.set_xlim(start_time, action_line_end[0])

# Get handles and labels from both axes
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Combine handles and labels
handles = handles1 + handles2
labels = labels1 + labels2

# Create a single legend at the bottom
fig.legend(handles, labels, loc='lower center', ncol=len(handles)/2, fontsize='small')
plt.subplots_adjust(bottom=.8)

# Display the plot
plt.tight_layout(pad=5)
plt.show()
plt.savefig(f'{csvfile}.eps')
plt.savefig(f'{csvfile}.pdf')
plt.savefig(f'{csvfile}.webp')
