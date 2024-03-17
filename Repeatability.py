# Assume robot is a connected and calibrated instance of your robot's control object

# Define a reference pose (could be any pose within the robot's operational envelope)
reference_pose = [0.2, 0.0, 0.2, 0.0, 0.0, 0.0]

# Number of repetitions for the test
repetitions = 250

# Store final poses for analysis
final_poses = []

for i in range(repetitions):
    # Move to the reference pose
    robot.move_pose(reference_pose)
    
    # Optionally, move back to an initial pose or neutral position if required for your test setup
    
    # Record the final pose
    final_pose = robot.get_pose()  # Assuming get_pose() returns a list or similar iterable
    final_poses.append(final_pose)

# Analysis - simple example calculating variance or deviation from the reference
# This part depends on how get_pose() returns data and may require adjustment
deviations = [((pose[0] - reference_pose[0])**2 + (pose[1] - reference_pose[1])**2 + (pose[2] - reference_pose[2])**2)**0.5 for pose in final_poses]
average_deviation = sum(deviations) / len(deviations)

print(f"Average deviation from reference pose: {average_deviation:.4f} meters")
