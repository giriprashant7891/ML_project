import ast
import pprint
import string
import json

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

data_file = 'D:\Downloads\yelp_dataset_challenge_academic_dataset\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_business.json'
out_file = 'data_files/yelp_academic_dataset_business_LV.json'

selected_city = 'Las Vegas'

print("Reading the business file")
out = open(out_file, 'w')
business_id_set = set()
# city_list = dict()

with open(data_file, 'r') as file:
    for line in file:
        business_id = line.split(',')[0].split(':')[1]
        # json_acceptable_string = line.replace("'", "\"")
        # data = json.loads(json_acceptable_string)
        # print json_acceptable_string
        # temp_dict = ast.literal_eval(json_acceptable_string)

        city = line.split('"city": ')[1].split(',')[0][1:-1]
        # if city in city_list:
        #     city_list[city] += 1
        # else:
        #     city_list[city] = 1

        if city == selected_city:
            business_id_set.add(business_id)
            out.write(line)

out.close()
# pprint.pprint(city_list)
# max_key = max(city_list, key=city_list.get)
# max_value = city_list[max_key]
# print(max_value, max_key)

review_file = 'D:\Downloads\yelp_dataset_challenge_academic_dataset\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_review.json'
out_file = 'data_files/yelp_academic_dataset_review_LV.json'

print("Reading the reviews file")
out = open(out_file, 'w')
with open(review_file, 'r') as file:
    for line in file:
        business_id = line.split(',')[-1].split(':')[1]
        business_id = business_id[:-2]
        if business_id in business_id_set:
            # print business_id
            out.write(line)

out.close()

review_file = 'D:\Downloads\yelp_dataset_challenge_academic_dataset\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_checkin.json'
out_file = 'data_files/yelp_academic_dataset_checkin_LV.json'

print("Reading the check in file")
out = open(out_file, 'w')
with open(review_file, 'r') as file:
    for line in file:
        business_id = line.split(',')[-1].split(':')[1]
        business_id = business_id[:-2]
        if business_id in business_id_set:
            # print business_id
            out.write(line)

out.close()

# review_file = 'data_files/yelp_academic_dataset_tip.json'
# out_file = 'data_files/yelp_academic_dataset_tip_IL.json'
#
# print "Reading the tips file"
# out = open(out_file, 'w')
# with open(review_file, 'r') as file:
#     for line in file:
#
#         business_id = line.split('business_id')[1].split(':')[1].split(',')[0].strip().lstrip()
#         if business_id in business_id_set:
#             # print business_id
#             out.write(line)
#
# out.close()

