import matplotlib.pyplot as plt
import datetime

business_file = 'data_files/yelp_academic_dataset_business_LV.json'
review_file = 'data_files/yelp_academic_dataset_review_LV.json'
review_file_2 = 'D:\Downloads\yelp_dataset_challenge_academic_dataset\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_review.json'

business_ids = dict()
with open(review_file, 'r') as file:
    for line in file:
        business_id = line.split(',')[-1].split(':')[1].lstrip().rstrip()[1:]
        business_id = business_id[:-2]

        if business_id in business_ids:
            business_ids[business_id] += 1
        else:
            business_ids[business_id] = 1


# Find the max value in the set
max_key = max(business_ids, key=business_ids.get)
max_value = business_ids[max_key]
print(max_value, max_key)

# Go back and plot the reviews for that business
date_list = []
star_list = []
with open(review_file, 'r') as file:
    for line in file:
        business_id = line.split(',')[-1].split(':')[1].lstrip().rstrip()[1:]
        business_id = business_id[:-2]

        if business_id == max_key:
            temp_dict = eval(line)
            star_list.append(float(temp_dict["stars"]))
            date = datetime.datetime.strptime(temp_dict["date"], "%Y-%m-%d")
            date_list.append(date)


star_list = [x for (y, x) in sorted(zip(date_list, star_list))]
date_list.sort()

# Find the moving average over x months
num_months_avg = 2

current_base = 0
i = 1
avg_date_list = []
avg_star_list = []
while True:
    diff = (date_list[i] - date_list[current_base]).days/30.0

    if diff > num_months_avg:
        avg_star_list.append(sum(star_list[current_base:i])/(i - current_base + 1))
        inc = int((date_list[i] - date_list[current_base]).days/2)
        avg_date_list.append(date_list[current_base] + datetime.timedelta(days=inc))
        current_base = i

    i += 1
    if i == len(date_list)-1:
        avg_star_list.append(sum(star_list[current_base:i])/(i - current_base + 1))
        inc = int((date_list[i] - date_list[current_base]).days/2)
        avg_date_list.append(date_list[current_base] + datetime.timedelta(days=inc))
        break


x_lim = [datetime.date(2005, 1, 1), datetime.date(2016, 1, 1)]
fig, (plot_d, plot_avg) = plt.subplots(1, 2)
plot_d.plot_date(date_list, star_list)
plot_d.grid(True)
plot_d.set_xlim(x_lim)
plot_d.set_ylim([0, 5.5])
plot_d.set_title('Raw data')
plot_avg.plot_date(avg_date_list, avg_star_list, '-')
plot_avg.grid(True)
plot_avg.set_xlim(x_lim)
plot_avg.set_ylim([0, 5.5])
plot_avg.set_title('Raw data averaged over a time period of %d months to see the trend' % num_months_avg)

plt.show()

