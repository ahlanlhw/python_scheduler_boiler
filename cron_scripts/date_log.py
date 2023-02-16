def log_date(cron_job):
    from datetime import datetime as dt
    import os
    date = dt.strftime(dt.now(),"%c")
    doc_title = '../logs/'+dt.strftime(dt.now(),"%Y%m%d")+".txt"
    with open(doc_title,'a') as f:
        f.write(f"{date} : Cron Job running {cron_job} \n")

