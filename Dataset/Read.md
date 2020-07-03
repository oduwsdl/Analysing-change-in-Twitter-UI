## Our Dataset

Our dataset consist of six different HAR files and other intermediate files that were created in the process of our analysis.

#### HAR files

The HAR files contain the network traffic data we captured for a duration of two minutes using the chrome developer tools. 

1. old_live.har - Contains network traffic for the live version of old Twitter UI. (Incognito mode with user-agent set as "Googlebot")
2. new_live_1.har - Contains network traffic for the live version of new Twitter UI. (Basic browser mode with default user-agent)
3. new_live_2.har - Contains network traffic for the live version of new Twitter UI. (Basic browser mode with user-agent set as "Googlebot") 
4. archived_1.har - Contains network traffic for the archived version of Twitter. (Archived through "SPN" of Internet Archive by us)
5. archived_2.har - Contains network traffic for the archived version of Twitter. (Archived through "SPN" of Internet Archive by other)
6. archived_3.har - Contains network traffic for the archived version of Twitter. (Archived using "curl" with user-agent set as "Googlebot")

The above mentioned HAR files can be downloaded from the release assets of this repository. Below are the respective target URLs for collecting network traffic.

1. old_live.har, new_live_1.har, new_live_2.har - https://twitter.com/realDonaldTrump
1. archived_1.har - http://web.archive.org/web/20200628012605/https://twitter.com/realDonaldTrump
2. archived_2.har - http://web.archive.org/web/20200628002632/https://twitter.com/realDonaldTrump
3. archived_3.har - http://web.archive.org/web/20200628015539/https://twitter.com/realDonaldTrump


#### TSV files

The TSV files contain the output from the har_analyser.py. Each file contain the "Date time", "URL", "Status Code", "Method", and "Mime Type" for each request.

1. old_live.tsv
2. new_live_1.tsv
3. new_live_2.tsv
4. archived_1.tsv
5. archived_2.tsv
6. archived_3.tsv

#### Unique URLs

The text files contain the unique URLs/Requests in each HAR file.

1. old_live.txt
2. new_live_1.txt
3. new_live_2.txt
4. archived_1.txt
5. archived_2.txt
6. archived_3.txt

#### Comm command output file

The below text files contain the comm utility output for comparing the requests between two files.

1. old_liveVSnew_live_1 - Old live vs New live
2. old_liveVSnew_live_2 - Old live (Googlebot) vs New live Googlebot
2. new_live_1VSnew_live_2 - New live vs New live Googlebot
3. archived_1VSarchived_2 - Archived SPN by us vs other
4. archived_1VSarchived_3 - Archived spn by us vs curl Googlebot
