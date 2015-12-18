# coding: utf-8
from app import db
from sqlalchemy import BigInteger, Column, Float, Index, Integer, LargeBinary, SmallInteger, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class AcctCoordTable(db.Model):
    __tablename__ = 'acct_coord_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    acct = Column(String, primary_key=True, nullable=False)
    user = Column(String, primary_key=True, nullable=False, index=True)


class AcctTable(Base):
    __tablename__ = 'acct_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    name = Column(String, primary_key=True)
    description = Column(Text, nullable=False)
    organization = Column(Text, nullable=False)


class AlbaAssocTable(Base):
    __tablename__ = 'alba_assoc_table'
    __table_args__ = (
        Index('user', 'user', 'acct', 'partition', unique=True),
    )

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    is_def = Column(Integer, nullable=False, server_default=text("'0'"))
    id_assoc = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    acct = Column(String, nullable=False, index=True)
    partition = Column(String, nullable=False)
    parent_acct = Column(String, nullable=False)
    lft = Column(Integer, nullable=False, index=True)
    rgt = Column(Integer, nullable=False)
    shares = Column(Integer, nullable=False, server_default=text("'1'"))
    max_jobs = Column(Integer)
    max_submit_jobs = Column(Integer)
    max_tres_pj = Column(Text, nullable=False)
    max_tres_pn = Column(Text, nullable=False)
    max_tres_mins_pj = Column(Text, nullable=False)
    max_tres_run_mins = Column(Text, nullable=False)
    max_wall_pj = Column(Integer)
    grp_jobs = Column(Integer)
    grp_submit_jobs = Column(Integer)
    grp_tres = Column(Text, nullable=False)
    grp_tres_mins = Column(Text, nullable=False)
    grp_tres_run_mins = Column(Text, nullable=False)
    grp_wall = Column(Integer)
    def_qos_id = Column(Integer)
    qos = Column(LargeBinary, nullable=False)
    delta_qos = Column(LargeBinary, nullable=False)


class AlbaAssocUsageDayTable(Base):
    __tablename__ = 'alba_assoc_usage_day_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True, nullable=False)
    id_tres = Column(Integer, primary_key=True, nullable=False, server_default=text("'1'"))
    time_start = Column(Integer, primary_key=True, nullable=False)
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaAssocUsageHourTable(Base):
    __tablename__ = 'alba_assoc_usage_hour_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True, nullable=False)
    id_tres = Column(Integer, primary_key=True, nullable=False, server_default=text("'1'"))
    time_start = Column(Integer, primary_key=True, nullable=False)
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaAssocUsageMonthTable(Base):
    __tablename__ = 'alba_assoc_usage_month_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True, nullable=False)
    id_tres = Column(Integer, primary_key=True, nullable=False, server_default=text("'1'"))
    time_start = Column(Integer, primary_key=True, nullable=False)
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaEventTable(Base):
    __tablename__ = 'alba_event_table'

    time_start = Column(Integer, primary_key=True, nullable=False)
    time_end = Column(Integer, nullable=False, server_default=text("'0'"))
    node_name = Column(String, primary_key=True, nullable=False)
    cluster_nodes = Column(Text, nullable=False)
    reason = Column(String, nullable=False)
    reason_uid = Column(Integer, nullable=False, server_default=text("'4294967294'"))
    state = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    tres = Column(Text, nullable=False)


class AlbaJobTable(Base):
    __tablename__ = 'alba_job_table'
    __table_args__ = (
        Index('sacct_def2', 'id_user', 'time_end', 'time_eligible'),
        Index('sacct_def', 'id_user', 'time_start', 'time_end'),
        Index('id_job', 'id_job', 'id_assoc', 'time_submit', unique=True),
        Index('rollup', 'time_eligible', 'time_end'),
        Index('rollup2', 'time_end', 'time_eligible')
    )

    job_db_inx = Column(Integer, primary_key=True)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    account = Column(String)
    array_task_str = Column(Text)
    array_max_tasks = Column(Integer, nullable=False, server_default=text("'0'"))
    array_task_pending = Column(Integer, nullable=False, server_default=text("'0'"))
    cpus_req = Column(Integer, nullable=False)
    derived_ec = Column(Integer, nullable=False, server_default=text("'0'"))
    derived_es = Column(Text)
    exit_code = Column(Integer, nullable=False, server_default=text("'0'"))
    job_name = Column(String, nullable=False)
    id_assoc = Column(Integer, nullable=False, index=True)
    id_array_job = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    id_array_task = Column(Integer, nullable=False, server_default=text("'4294967294'"))
    id_block = Column(String)
    id_job = Column(Integer, nullable=False)
    id_qos = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    id_resv = Column(Integer, nullable=False, index=True)
    id_wckey = Column(Integer, nullable=False, index=True)
    id_user = Column(Integer, nullable=False)
    id_group = Column(Integer, nullable=False)
    kill_requid = Column(Integer, nullable=False, server_default=text("'-1'"))
    mem_req = Column(Integer, nullable=False, server_default=text("'0'"))
    nodelist = Column(Text)
    nodes_alloc = Column(Integer, nullable=False, index=True)
    node_inx = Column(Text)
    partition = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    state = Column(SmallInteger, nullable=False)
    timelimit = Column(Integer, nullable=False, server_default=text("'0'"))
    time_submit = Column(Integer, nullable=False, server_default=text("'0'"))
    time_eligible = Column(Integer, nullable=False, server_default=text("'0'"))
    time_start = Column(Integer, nullable=False, server_default=text("'0'"))
    time_end = Column(Integer, nullable=False, server_default=text("'0'"))
    time_suspended = Column(Integer, nullable=False, server_default=text("'0'"))
    gres_req = Column(Text, nullable=False)
    gres_alloc = Column(Text, nullable=False)
    gres_used = Column(Text, nullable=False)
    wckey = Column(String, nullable=False)
    track_steps = Column(Integer, nullable=False)
    tres_alloc = Column(Text, nullable=False)
    tres_req = Column(Text, nullable=False)


class AlbaLastRanTable(Base):
    __tablename__ = 'alba_last_ran_table'

    hourly_rollup = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    daily_rollup = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    monthly_rollup = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))


class AlbaResvTable(Base):
    __tablename__ = 'alba_resv_table'

    id_resv = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    assoclist = Column(Text, nullable=False)
    flags = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    nodelist = Column(Text, nullable=False)
    node_inx = Column(Text, nullable=False)
    resv_name = Column(Text, nullable=False)
    time_start = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    time_end = Column(Integer, nullable=False, server_default=text("'0'"))
    tres = Column(Text, nullable=False)


class AlbaStepTable(Base):
    __tablename__ = 'alba_step_table'

    job_db_inx = Column(Integer, primary_key=True, nullable=False)
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    exit_code = Column(Integer, nullable=False, server_default=text("'0'"))
    id_step = Column(Integer, primary_key=True, nullable=False)
    kill_requid = Column(Integer, nullable=False, server_default=text("'-1'"))
    nodelist = Column(Text, nullable=False)
    nodes_alloc = Column(Integer, nullable=False)
    node_inx = Column(Text)
    state = Column(SmallInteger, nullable=False)
    step_name = Column(Text, nullable=False)
    task_cnt = Column(Integer, nullable=False)
    task_dist = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    time_start = Column(Integer, nullable=False, server_default=text("'0'"))
    time_end = Column(Integer, nullable=False, server_default=text("'0'"))
    time_suspended = Column(Integer, nullable=False, server_default=text("'0'"))
    user_sec = Column(Integer, nullable=False, server_default=text("'0'"))
    user_usec = Column(Integer, nullable=False, server_default=text("'0'"))
    sys_sec = Column(Integer, nullable=False, server_default=text("'0'"))
    sys_usec = Column(Integer, nullable=False, server_default=text("'0'"))
    max_pages = Column(Integer, nullable=False, server_default=text("'0'"))
    max_pages_task = Column(Integer, nullable=False, server_default=text("'0'"))
    max_pages_node = Column(Integer, nullable=False, server_default=text("'0'"))
    ave_pages = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    max_rss = Column(BigInteger, nullable=False, server_default=text("'0'"))
    max_rss_task = Column(Integer, nullable=False, server_default=text("'0'"))
    max_rss_node = Column(Integer, nullable=False, server_default=text("'0'"))
    ave_rss = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    max_vsize = Column(BigInteger, nullable=False, server_default=text("'0'"))
    max_vsize_task = Column(Integer, nullable=False, server_default=text("'0'"))
    max_vsize_node = Column(Integer, nullable=False, server_default=text("'0'"))
    ave_vsize = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    min_cpu = Column(Integer, nullable=False, server_default=text("'4294967294'"))
    min_cpu_task = Column(Integer, nullable=False, server_default=text("'0'"))
    min_cpu_node = Column(Integer, nullable=False, server_default=text("'0'"))
    ave_cpu = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    act_cpufreq = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    consumed_energy = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    req_cpufreq_min = Column(Integer, nullable=False, server_default=text("'0'"))
    req_cpufreq = Column(Integer, nullable=False, server_default=text("'0'"))
    req_cpufreq_gov = Column(Integer, nullable=False, server_default=text("'0'"))
    max_disk_read = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    max_disk_read_task = Column(Integer, nullable=False, server_default=text("'0'"))
    max_disk_read_node = Column(Integer, nullable=False, server_default=text("'0'"))
    ave_disk_read = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    max_disk_write = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    max_disk_write_task = Column(Integer, nullable=False, server_default=text("'0'"))
    max_disk_write_node = Column(Integer, nullable=False, server_default=text("'0'"))
    ave_disk_write = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    tres_alloc = Column(Text, nullable=False)


class AlbaSuspendTable(Base):
    __tablename__ = 'alba_suspend_table'
    __table_args__ = (
        Index('job_db_inx_times', 'job_db_inx', 'time_start', 'time_end'),
    )

    job_db_inx = Column(Integer, primary_key=True, nullable=False)
    id_assoc = Column(Integer, nullable=False)
    time_start = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    time_end = Column(Integer, nullable=False, server_default=text("'0'"))


class AlbaUsageDayTable(Base):
    __tablename__ = 'alba_usage_day_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id_tres = Column(Integer, primary_key=True, nullable=False)
    time_start = Column(Integer, primary_key=True, nullable=False)
    count = Column(BigInteger, nullable=False, server_default=text("'0'"))
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    down_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    pdown_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    idle_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    resv_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    over_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaUsageHourTable(Base):
    __tablename__ = 'alba_usage_hour_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id_tres = Column(Integer, primary_key=True, nullable=False)
    time_start = Column(Integer, primary_key=True, nullable=False)
    count = Column(BigInteger, nullable=False, server_default=text("'0'"))
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    down_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    pdown_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    idle_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    resv_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    over_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaUsageMonthTable(Base):
    __tablename__ = 'alba_usage_month_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id_tres = Column(Integer, primary_key=True, nullable=False)
    time_start = Column(Integer, primary_key=True, nullable=False)
    count = Column(BigInteger, nullable=False, server_default=text("'0'"))
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    down_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    pdown_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    idle_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    resv_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))
    over_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaWckeyTable(Base):
    __tablename__ = 'alba_wckey_table'
    __table_args__ = (
        Index('wckey_name', 'wckey_name', 'user', unique=True),
    )

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    is_def = Column(Integer, nullable=False, server_default=text("'0'"))
    id_wckey = Column(Integer, primary_key=True)
    wckey_name = Column(String, nullable=False)
    user = Column(String, nullable=False)


class AlbaWckeyUsageDayTable(Base):
    __tablename__ = 'alba_wckey_usage_day_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True, nullable=False)
    id_tres = Column(Integer, primary_key=True, nullable=False, server_default=text("'1'"))
    time_start = Column(Integer, primary_key=True, nullable=False)
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaWckeyUsageHourTable(Base):
    __tablename__ = 'alba_wckey_usage_hour_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True, nullable=False)
    id_tres = Column(Integer, primary_key=True, nullable=False, server_default=text("'1'"))
    time_start = Column(Integer, primary_key=True, nullable=False)
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class AlbaWckeyUsageMonthTable(Base):
    __tablename__ = 'alba_wckey_usage_month_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True, nullable=False)
    id_tres = Column(Integer, primary_key=True, nullable=False, server_default=text("'1'"))
    time_start = Column(Integer, primary_key=True, nullable=False)
    alloc_secs = Column(BigInteger, nullable=False, server_default=text("'0'"))


class ClusResTable(Base):
    __tablename__ = 'clus_res_table'
    __table_args__ = (
        Index('res_id', 'res_id', 'cluster', unique=True),
    )

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    cluster = Column(String, primary_key=True, nullable=False)
    res_id = Column(Integer, primary_key=True, nullable=False)
    percent_allowed = Column(Integer, server_default=text("'0'"))


class ClusterTable(Base):
    __tablename__ = 'cluster_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    name = Column(String, primary_key=True)
    control_host = Column(String, nullable=False)
    control_port = Column(Integer, nullable=False, server_default=text("'0'"))
    last_port = Column(Integer, nullable=False, server_default=text("'0'"))
    rpc_version = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    classification = Column(SmallInteger, server_default=text("'0'"))
    dimensions = Column(SmallInteger, server_default=text("'1'"))
    plugin_id_select = Column(SmallInteger, server_default=text("'0'"))
    flags = Column(Integer, server_default=text("'0'"))


class QosTable(Base):
    __tablename__ = 'qos_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    flags = Column(Integer, server_default=text("'0'"))
    grace_time = Column(Integer)
    max_jobs_per_user = Column(Integer)
    max_submit_jobs_per_user = Column(Integer)
    max_tres_pj = Column(Text, nullable=False)
    max_tres_pn = Column(Text, nullable=False)
    max_tres_pu = Column(Text, nullable=False)
    max_tres_mins_pj = Column(Text, nullable=False)
    max_tres_run_mins_pu = Column(Text, nullable=False)
    min_tres_pj = Column(Text, nullable=False)
    max_wall_duration_per_job = Column(Integer)
    grp_jobs = Column(Integer)
    grp_submit_jobs = Column(Integer)
    grp_tres = Column(Text, nullable=False)
    grp_tres_mins = Column(Text, nullable=False)
    grp_tres_run_mins = Column(Text, nullable=False)
    grp_wall = Column(Integer)
    preempt = Column(Text, nullable=False)
    preempt_mode = Column(Integer, server_default=text("'0'"))
    priority = Column(Integer, server_default=text("'0'"))
    usage_factor = Column(Float(asdecimal=True), nullable=False, server_default=text("'1'"))
    usage_thres = Column(Float(asdecimal=True))


class ResTable(Base):
    __tablename__ = 'res_table'
    __table_args__ = (
        Index('name', 'name', 'server', 'type', unique=True),
    )

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    manager = Column(String, nullable=False)
    server = Column(String, nullable=False)
    count = Column(Integer, server_default=text("'0'"))
    type = Column(Integer, server_default=text("'0'"))
    flags = Column(Integer, server_default=text("'0'"))


class TableDefsTable(Base):
    __tablename__ = 'table_defs_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    table_name = Column(Text, primary_key=True)
    definition = Column(Text, nullable=False)


class TresTable(Base):
    __tablename__ = 'tres_table'
    __table_args__ = (
        Index('type', 'type', 'name', unique=True),
    )

    creation_time = Column(Integer, nullable=False)
    deleted = Column(Integer, nullable=False, server_default=text("'0'"))
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)


class TxnTable(Base):
    __tablename__ = 'txn_table'

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer, nullable=False, server_default=text("'0'"))
    action = Column(SmallInteger, nullable=False)
    name = Column(Text, nullable=False)
    actor = Column(String, nullable=False)
    cluster = Column(String, nullable=False)
    info = Column(LargeBinary)


class UserTable(Base):
    __tablename__ = 'user_table'

    creation_time = Column(Integer, nullable=False)
    mod_time = Column(Integer, nullable=False, server_default=text("'0'"))
    deleted = Column(Integer, server_default=text("'0'"))
    name = Column(String, primary_key=True)
    admin_level = Column(SmallInteger, nullable=False, server_default=text("'1'"))
