#
#
#  Basic for scraping data from static pages
#
# ------ IMPORTANT! ------
# if you need return soup object:
# you cand import from __utils -> GetHtmlSoup
# if you need return regex object:
# you cand import from __utils ->
# ---> get_data_with_regex(expression: str, object: str)
#
# Company ---> Voxility
# Link ------> https://www.voxility.com/jobs
#
#
from __utils import (
    GetStaticSoup,
    get_county,
    get_job_type,
    Item,
    UpdateAPI,
)





def scraper():
    '''
    ... scrape data from Voxility scraper.
    '''
    base_link = "https://www.voxility.com/jobs" 
    soup = GetStaticSoup(base_link)

    job_list = []
    for job in soup.find_all('h4', attrs={'job-title'}):
        
        #check if job tipe contain in job title
        # if 'hybrid' in job.find('a').text.lower():
        #    job_type='hybrid'
        # elif 'remote' in job.find('a').text.lower():
        #     job_type='remote'
        # else:
        #     job_type=''
        print(job.find('a').text.lower())
        print(get_job_type(job.find('a').text.lower()))
        
       #extract location from job_location and replace bucharest to Bucuresti
        if (location := job.find('span', attrs={'job-location'}).text.split()[-2].replace(',','').lower() in ['bucharest']):
            location ='București'
        
        finish_location=get_county(location)

        # get jobs items from response
        job_list.append(Item(
            job_title = job.find('a').text,
            job_link = base_link + job.find('a',)['href'].replace('..',''),
            company='Voxility',
            country='Romania',
            county = finish_location[0] if True in finish_location  else None,
            city='all' if location.lower() == finish_location[0].lower() and finish_location[0].lower() !='bucuresti' else finish_location[0],
            remote = ''#get_job_type(job_type),
        ).to_dict())

    return job_list


def main():
    '''
    ... Main:
    ---> call scraper()
    ---> update_jobs() and update_logo()
    '''

    company_name = "Voxility"
    logo_link = "https://www.voxility.com/public/themes/mobile_VoxilityLogo.png"

    jobs = scraper()
    
    # uncomment if your scraper done
    # UpdateAPI().update_jobs(company_name, jobs)
    # UpdateAPI().update_logo(company_name, logo_link)


if __name__ == '__main__':
    main()
