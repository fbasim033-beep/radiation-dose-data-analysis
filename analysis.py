import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic radiation dose data for 100 patients
np.random.seed(42)
patient_ids = np.arange(1, 101)
dose_values = np.random.normal(loc=50, scale=5, size=100)  # mean=50 Gy, std=5 Gy

data = pd.DataFrame({
    "Patient_ID": patient_ids,
    "Radiation_Dose_Gy": dose_values
})

# Save dataset
data.to_csv("radiation_dose_data.csv", index=False)

# Basic statistics
mean_dose = data["Radiation_Dose_Gy"].mean()
std_dose = data["Radiation_Dose_Gy"].std()
max_dose = data["Radiation_Dose_Gy"].max()
min_dose = data["Radiation_Dose_Gy"].min()

print("Radiation Dose Statistics:")
print(f"Mean Dose: {mean_dose:.2f} Gy")
print(f"Standard Deviation: {std_dose:.2f} Gy")
print(f"Maximum Dose: {max_dose:.2f} Gy")
print(f"Minimum Dose: {min_dose:.2f} Gy")

# Plot distribution
plt.hist(data["Radiation_Dose_Gy"], bins=10)
plt.title("Radiation Dose Distribution")
plt.xlabel("Dose (Gy)")
plt.ylabel("Number of Patients")
plt.show()
