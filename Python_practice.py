voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

# items()
# [["county", "Arapahoe"], ["registered_voters", 422829]]


for values in voting_data:
    county = values["county"]
    registered_voters = values["registered_voters"]
    print(f"{county} has this many voters {registered_voters:,.2f}")
   
with open(file_to_save, "w") as txt_file:
   