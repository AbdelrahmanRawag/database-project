# Project : database
  
  # Table of Contents
 **1**.Overview  
 **2**.Content  
 **3**.Running the App
  
  # Overview
  taking about Veiwing result of queries 
  # Content
 **1**.Main.py
# Running the App
To start the application wirte these queries to create these views:
  * 1-create view m_articles as select title , count (log.id) as koko from articles , log where status ='200 OK' and path like concat( concat ('%', slug),'%') group by title order by koko ;
  * 2-create view m_authors as  select name , count (log.id) as koko from articles , log , authors where status ='200 OK' and path like concat( concat ('%', slug),'%') and articles.author = authors.id group by name order by koko ;
  * 3-create view dates_errors as select Date(time) date , count(status) as total_requests , count (case when status !='200 OK' then 1 else null end) as errors from log group by date ;

Run Main.py from Vagrant 
