from app import app,db
from app import models
from models import AlbaAssocTable,AlbaJobTable,AlbaUsageMonthTable
from flask import render_template
from datetime import date, timedelta
from calendar import timegm
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy



@app.route('/')
@app.route('/index')
def index():
    #return render_template('test.html',title='Home',users=user)

    prevMonth = timegm((date.today().replace(day=1) - timedelta(days=1)).timetuple())
    prevMonth = '1446332399'
    monthCPU = db.session.query(AlbaUsageMonthTable.alloc_secs).filter(AlbaUsageMonthTable.creation_time > prevMonth). \
        filter(AlbaUsageMonthTable.id_tres=='1').first()[0]
    nMonthJobs=db.session.query(func.count(AlbaAssocTable.creation_time)).filter(AlbaAssocTable.creation_time > prevMonth).first()[0]
    return render_template('index.html',nMonthJobs=nMonthJobs,monthCPU=('%.2f'%(monthCPU/3600)))


@app.context_processor
def utility_processor():
    def job_state(state):
        return {
            0:"JOB_PENDING",
            1:"JOB_RUNNING",
            2:"JOB_SUSPENDED",
            3:"JOB_COMPLETE",
            4:"JOB_CANCELLED",
            5:"JOB_FAILED",
            6:"JOB_TIMEOUT",
            7:"JOB_NODE_FAIL",
            8:"JOB_END"
        }[state]
    return dict(job_state=job_state)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

