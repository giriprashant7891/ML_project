import operator
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime

business_file = 'data_files/yelp_academic_dataset_business_IL.json'
review_file = 'data_files/yelp_academic_dataset_review_IL.json'
review_file_2 = 'D:\Downloads\yelp_dataset_challenge_academic_dataset\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_review.json'

business_ids = dict()
with open(review_file_2, 'r') as file:
    for line in file:
        business_id = line.split(',')[-1].split(':')[1].lstrip().rstrip()
        business_id = business_id[:-2]

        if business_id in business_ids:
            business_ids[business_id] += 1
        else:
            business_ids[business_id] = 1


# Find the max value in the set
max_key = max(business_ids, key=business_ids.get)
max_value = business_ids[max_key]
print(max_value, max_key)

# max_key = '"4bEjOyTaDG24SY5TxsaUNQ'
# Go back and plot the reviews for that business

date_list = []
star_list = []
with open(review_file_2, 'r') as file:
    for line in file:
        business_id = line.split(',')[-1].split(':')[1].lstrip().rstrip()
        business_id = business_id[:-2]

        if business_id == max_key:
            temp_dict = eval(line)
            star_list.append(float(temp_dict["stars"]))
            date = datetime.datetime.strptime(temp_dict["date"], "%Y-%m-%d")
            date_list.append(date)


# dates = (date_list)
x_lim = [datetime.date(2005, 1, 1), datetime.date(2016, 1, 1)]
fig, plot_d = plt.subplots()
plot_d.plot_date(date_list, star_list)
plot_d.grid(True)
plot_d.set_xlim(x_lim)
plot_d.set_ylim([0, 5.5])
plt.show()

