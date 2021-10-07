import requests
import csv
from bs4 import BeautifulSoup

# Function: Goes through list of fighter links and
# To Fix/Add:
# - better data type collection
#   - change height value to feet and inches
#   - remove " from reach value
#   - remove f_link column
#   - bool_curr_belt to curr_belt(bool type)
#   - new table on mariadb 
# - collecting other fighter data
#   - height 
#   - more detailed statistics
# - automation
#   - run at regular intervals
#   - auto update database


dir_urls = []

# helper function to remove prefix
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

# append directory urls to array
with open("abc_urls.txt","r") as abc_urls:
    for line in abc_urls:
        dir_urls.append(line.replace("\n",""))

# prep csv_writer
filename = "fighter_info.csv"
csv_writer = csv.writer(open(filename, "w", newline = ""))

# write headers to csv file
headers = ['f_link','f_id','firstname','lastname','nickname','Height','Weight','Reach','Stance','Wins','Losses','Draws','bool_curr_belt']
csv_writer.writerow(headers)

f_links = []
f_ids = []
f_count = 0
pages_crawled = 0

# Loops through alphabetized pages of the fighter directory
for link in dir_urls:
    # prep bs4
    URL = link
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")


    f_rows = soup.find_all("tr", class_= "b-statistics__table-row")

    for row in f_rows:

        data = []

        find_a = row.find_all(href=True)

        # finds and appends fighter link and fighter id to data
        # if no link is found, skips row and continues to the next
        if find_a:
            for a in find_a:
                f_link = (a['href'])
                # appends fighter link to data
                data.append(f_link)
                # updates list of fighter links
                f_links.append(f_link)
                # updates list of fighter ids
                #f_id = f_link.strip("http://ufcstats.com/fighter-details/")
                f_id = remove_prefix(f_link, "http://ufcstats.com/fighter-details/")
                f_ids.append(f_id)
                data.append(f_id)
                #increments fighter count
                f_count += 1
                break
        else:
            continue

        cols = row.find_all(class_ = "b-statistics__table-col")

        # updates data with fighter info
        for col in cols:
            find_b = col.find(class_ = "b-list__icon")

            if find_b:
                data.append("1")
            else:
                #element = col.text.strip()
                #data.append(element.replace("\\","")
                data.append(col.text.strip())

        csv_writer.writerow(data)
        #print(data)

    with open('fighter_links.txt', 'w') as f:
        for item in f_links:
            f.write(item)
            f.write('\n')

    with open('fighter_ids.txt', 'w') as f:
        for item in f_ids:
            f.write(item)
            f.write('\n')

    # increment pages crawled
    pages_crawled += 1
    str_pages = str(pages_crawled)
    
    print("Number of Pages Crawled: " + str_pages + "/26\n")
    


#print(f_links)
#print(f_ids)
str_f_count = str(f_count) 
print("\n\nNumber of Fighters Crawled: " + str_f_count)

    


        
        
        
        

    

    
    
    
    
    
