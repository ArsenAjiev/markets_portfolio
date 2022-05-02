Data Analysis
====

## Start use sqlite3

```shell
   pip3 install -r requirements.txt
   python3 manage.py migrate
   python3 manage.py createsuperuser 
```

1. Create "country" - Open a browser to `http://127.0.0.1:8000/airpollution/temp_country_creator/` 
2. Update color in "country" - Open a browser to `http://127.0.0.1:8000/airpollution/temp_country_creator/?update=true` 
3. Upload Data (3 excels files) in `http://127.0.0.1:8000/airpollution/`
4. Update "pollutant" -  `http://127.0.0.1:8000/airpollution/temp_add_colors_to_pollutants`
5. Open a browser to `http://127.0.0.1:8000/airpollution/` 





1. Upload Data

   ![](./data_for_project/screenshot/upload_file.png)
   
2. Table Data

   ![](./data_for_project/screenshot/table_data.png)

3. Visual Data

   ![](./data_for_project/screenshot/visuals_data.png)

