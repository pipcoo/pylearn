# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String, Table, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class TBkOrder(Base):
    __tablename__ = 't_bk_order'

    cost_id = Column(Numeric(scale=0, asdecimal=False))
    create_time = Column(DateTime)
    order_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    seq = Column(String(50))
    total_amount = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    wechat_package = Column(String(50))
    wechat_user_id = Column(Numeric(scale=0, asdecimal=False))


class TBkOrderCost(Base):
    __tablename__ = 't_bk_order_cost'

    cost_amount = Column(Numeric(scale=0, asdecimal=False))
    cost_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    cost_status = Column(Numeric(scale=0, asdecimal=False))
    cost_time = Column(DateTime)
    cost_type = Column(Numeric(scale=0, asdecimal=False))
    deal_seq = Column(String(50))


class TBkOrderGood(Base):
    __tablename__ = 't_bk_order_good'

    base_price = Column(Numeric(scale=0, asdecimal=False))
    deposit_id = Column(Numeric(scale=0, asdecimal=False))
    extract_code = Column(String(8))
    good_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    notify_id = Column(Numeric(scale=0, asdecimal=False))
    order_id = Column(Numeric(scale=0, asdecimal=False))
    real_price = Column(Numeric(scale=0, asdecimal=False))
    refund_id = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    status = Column(Numeric(scale=0, asdecimal=False))
    valid_day = Column(String(10))
    vendout_id = Column(Numeric(scale=0, asdecimal=False))


class TBkOrderGoodDeposit(Base):
    __tablename__ = 't_bk_order_good_deposit'

    deposit_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    deposit_price = Column(Numeric(scale=0, asdecimal=False))
    refund_id = Column(Numeric(scale=0, asdecimal=False))


class TBkOrderGoodNotify(Base):
    __tablename__ = 't_bk_order_good_notify'

    notify_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    notify_status = Column(Numeric(scale=0, asdecimal=False))
    notify_time = Column(DateTime)
    order_good_id = Column(Numeric(scale=0, asdecimal=False))


class TBkOrderGoodVendout(Base):
    __tablename__ = 't_bk_order_good_vendout'

    order_good_id = Column(Numeric(scale=0, asdecimal=False))
    vendout_channel_id = Column(Numeric(scale=0, asdecimal=False))
    vendout_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    vendout_status = Column(Numeric(scale=0, asdecimal=False))
    vendout_time = Column(DateTime)


class TBkOrderRefund(Base):
    __tablename__ = 't_bk_order_refund'

    order_id = Column(Numeric(scale=0, asdecimal=False))
    refund_amount = Column(Numeric(scale=0, asdecimal=False))
    refund_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refund_seq = Column(String(50))
    refund_status = Column(Numeric(scale=0, asdecimal=False))
    refund_time = Column(DateTime)
    refund_type = Column(Numeric(scale=0, asdecimal=False))


class TErpDataSync(Base):
    __tablename__ = 't_erp_data_sync'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    data_content = Column(String(2000))
    data_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    data_type = Column(String(20))
    sync_mark = Column(Numeric(scale=0, asdecimal=False))
    sync_time = Column(DateTime)
    sync_url = Column(String(200))


class TMtArea(Base):
    __tablename__ = 't_mt_area'

    area_code = Column(String(10))
    area_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    area_level = Column(Numeric(scale=0, asdecimal=False))
    area_name = Column(String(50))
    p_id = Column(Numeric(scale=0, asdecimal=False))


class TMtBusinessDistrict(Base):
    __tablename__ = 't_mt_business_district'

    business_district_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    business_district_name = Column(String(50))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))


class TMtCompany(Base):
    __tablename__ = 't_mt_company'

    company_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    company_level = Column(Numeric(scale=0, asdecimal=False))
    company_name = Column(String(50))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    customer_id = Column(Numeric(scale=0, asdecimal=False))
    p_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    max_vm_capacity = Column(Numeric(9, 0, asdecimal=False))


class TMtCustomer(Base):
    __tablename__ = 't_mt_customer'

    collection_account = Column(String(50))
    collection_account_type = Column(String(200))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    customer_address = Column(String(100))
    customer_email = Column(String(50))
    customer_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    customer_mode = Column(Numeric(scale=0, asdecimal=False))
    customer_name = Column(String(50))
    customer_type = Column(Numeric(asdecimal=False))
    manager_name = Column(String(50))
    manager_phone = Column(String(20))
    sync_mark = Column(Numeric(scale=0, asdecimal=False))
    sync_time = Column(DateTime)
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    tax_code = Column(String(50))
    giro_account = Column(String(50))
    giro_account_type = Column(Numeric(scale=0, asdecimal=False))
    giro_account_name = Column(String(50))


class TMtCustomerSecret(Base):
    __tablename__ = 't_mt_customer_secret'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    customer_id = Column(Numeric(scale=0, asdecimal=False))
    customer_public_id = Column(String(10), nullable=False)
    key_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    key_value = Column(String(200))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))


class TMtHardware(Base):
    __tablename__ = 't_mt_hardware'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    hardware_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    hd_category = Column(String(100))
    hd_code = Column(String(30))
    hd_desc = Column(String(500))
    hd_name = Column(String(100))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))


class TMtNode(Base):
    __tablename__ = 't_mt_node'

    area_id = Column(Numeric(scale=0, asdecimal=False))
    business_district_id = Column(Numeric(scale=0, asdecimal=False))
    company_id = Column(Numeric(scale=0, asdecimal=False))
    delivery_id = Column(Numeric(scale=0, asdecimal=False))
    latitude = Column(String(12))
    fill_type = Column(Numeric(scale=0, asdecimal=False))
    longitude = Column(String(12))
    node_address = Column(String(300))
    node_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    node_name = Column(String(50))
    opt_end_time = Column(String(8))
    opt_start_time = Column(String(8))
    property_level = Column(String(20))
    property_name = Column(String(50))
    property_phone = Column(String(20))
    put_end_time = Column(String(8))
    put_method = Column(String(300))
    put_start_time = Column(String(8))
    repair_id = Column(Numeric(scale=0, asdecimal=False))
    city_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    province_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    property_manager = Column(String(50))
    partner_id = Column(Numeric(scale=0, asdecimal=False))
    longitude_mars = Column(String(12))
    latitude_mars = Column(String(12))


class TMtPartner(Base):
    __tablename__ = 't_mt_partner'

    collection_account = Column(String(50))
    collection_account_type = Column(String(200))
    company_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    manager_name = Column(String(50))
    manager_phone = Column(String(20))
    partner_address = Column(String(200))
    partner_email = Column(String(50))
    partner_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    partner_name = Column(String(100))
    partner_type = Column(Numeric(scale=0, asdecimal=False))
    tax_code = Column(String(50))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    ctor = Column(Numeric(asdecimal=False))


class TMtSim(Base):
    __tablename__ = 't_mt_sim'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    delete_mark = Column(Numeric(scale=0, asdecimal=False))
    service_provider = Column(Numeric(scale=0, asdecimal=False))
    sim_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sim_number = Column(String(20))
    sim_phone = Column(String(20))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtSku(Base):
    __tablename__ = 't_mt_sku'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    db_code = Column(String(50))
    img_url = Column(String(250))
    inventory_type = Column(String(50))
    offer_price = Column(Numeric(scale=0, asdecimal=False))
    packing_specification = Column(String(100))
    sku_code = Column(String(50))
    sku_color = Column(String(20))
    sku_desc = Column(String(500))
    sku_height = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sku_length = Column(Numeric(scale=0, asdecimal=False))
    sku_made_area = Column(String(200))
    sku_name = Column(String(50))
    sku_producer = Column(String(100))
    sku_type = Column(Numeric(scale=0, asdecimal=False))
    sku_unit = Column(String(50))
    sku_width = Column(Numeric(scale=0, asdecimal=False))
    storage_method = Column(String(200))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    sku_shelf_life = Column(Numeric(scale=0, asdecimal=False))
    sale_area = Column(String(200))
    deposit = Column(Numeric(scale=0, asdecimal=False))
    reserve = Column(Numeric(scale=0, asdecimal=False))


class TMtSkuCompany(Base):
    __tablename__ = 't_mt_sku_company'

    company_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sku_id = Column(Numeric(scale=0, asdecimal=False))


class TMtSkuType(Base):
    __tablename__ = 't_mt_sku_type'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    p_id = Column(Numeric(scale=0, asdecimal=False), server_default=text("0"))
    type_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    type_name = Column(String(50))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    external_id = Column(String(100))


class TMtTheme(Base):
    __tablename__ = 't_mt_theme'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    theme_desc = Column(String(500))
    theme_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    theme_name = Column(String(50))
    theme_url = Column(String(100))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    preview_urls = Column(String(300))
    delete_mark = Column(Numeric(scale=0, asdecimal=False))
    theme_md5 = Column(String(32))
    theme_size = Column(Numeric(scale=0, asdecimal=False))


class TMtUpgradeDetail(Base):
    __tablename__ = 't_mt_upgrade_detail'

    detaild_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    plan_id = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtUpgradePackage(Base):
    __tablename__ = 't_mt_upgrade_package'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    disable = Column(Numeric(scale=0, asdecimal=False))
    package_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    package_type = Column(Numeric(scale=0, asdecimal=False))
    package_version = Column(String(50))
    resource_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))


class TMtUpgradePlan(Base):
    __tablename__ = 't_mt_upgrade_plan'

    area_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    end_time = Column(String(10))
    package_id = Column(Numeric(scale=0, asdecimal=False))
    plan_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    start_time = Column(String(10))
    vm_model_id = Column(Numeric(scale=0, asdecimal=False))


class TMtUpgradeVersion(Base):
    __tablename__ = 't_mt_upgrade_version'

    last_downloaded_ver = Column(String(50))
    last_issued_ver = Column(Numeric(scale=0, asdecimal=False))
    last_req_ver = Column(String(50))
    version_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    version_type = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVm(Base):
    __tablename__ = 't_mt_vm'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    delete_mark = Column(Numeric(scale=0, asdecimal=False))
    inner_code = Column(String(20))
    node_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_desc = Column(String(200))
    vm_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    vm_model_id = Column(Numeric(scale=0, asdecimal=False))
    vm_status = Column(Numeric(1, 0, asdecimal=False))
    company_id = Column(Numeric(scale=0, asdecimal=False))
    hardware_code = Column(String(100))
    create_task_cycle = Column(Numeric(scale=0, asdecimal=False))
    unique_code = Column(String(32))
    channel_structure = Column(String(500))
    report_sp_count = Column(Numeric(scale=0, asdecimal=False))
    printer = Column(Numeric(scale=0, asdecimal=False))
    reserve = Column(Numeric(scale=0, asdecimal=False))


class TMtVmChannel(Base):
    __tablename__ = 't_mt_vm_channel'

    channel_code = Column(String(10))
    channel_height = Column(Numeric(scale=0, asdecimal=False))
    channel_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    channel_long = Column(Numeric(scale=0, asdecimal=False))
    channel_status = Column(Numeric(scale=0, asdecimal=False))
    channel_width = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    curr_num = Column(Numeric(scale=0, asdecimal=False))
    inner_code = Column(String(20))
    max_capacity = Column(Numeric(scale=0, asdecimal=False))
    merge_qty = Column(Numeric(scale=0, asdecimal=False))
    pc_type = Column(Numeric(scale=0, asdecimal=False))
    remarks = Column(String(200))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    accept_width_max = Column(Numeric(9, 0, asdecimal=False))
    display_mode = Column(Numeric(9, 0, asdecimal=False))
    fixed_capacity = Column(Numeric(9, 0, asdecimal=False))
    is_fixed_capacity = Column(Numeric(9, 0, asdecimal=False))
    merge_pid = Column(Numeric(9, 0, asdecimal=False))
    has_next_stock = Column(Numeric(scale=0, asdecimal=False))


class TMtVmChannelNext(Base):
    __tablename__ = 't_mt_vm_channel_next'

    channel_code = Column(String(10))
    channel_height = Column(Numeric(scale=0, asdecimal=False))
    channel_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    channel_long = Column(Numeric(scale=0, asdecimal=False))
    channel_status = Column(Numeric(scale=0, asdecimal=False))
    channel_width = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    inner_code = Column(String(20))
    max_capacity = Column(Numeric(scale=0, asdecimal=False))
    merge_qty = Column(Numeric(scale=0, asdecimal=False))
    pc_type = Column(Numeric(scale=0, asdecimal=False))
    remarks = Column(String(200))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    accept_width_max = Column(Numeric(9, 0, asdecimal=False))
    display_mode = Column(Numeric(9, 0, asdecimal=False))
    fixed_capacity = Column(Numeric(9, 0, asdecimal=False))
    is_fixed_capacity = Column(Numeric(9, 0, asdecimal=False))
    merge_pid = Column(Numeric(9, 0, asdecimal=False))


class TMtVmEnergySave(Base):
    __tablename__ = 't_mt_vm_energy_save'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    end_time = Column(String(8))
    energy_save_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    energy_save_type = Column(Numeric(scale=0, asdecimal=False))
    remark = Column(String(200))
    start_time = Column(String(8))
    target_value = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    temp_box_no = Column(Numeric(scale=0, asdecimal=False))


class TMtVmEvent(Base):
    __tablename__ = 't_mt_vm_event'

    discount_type = Column(Numeric(scale=0, asdecimal=False))
    discount_value = Column(Numeric(scale=0, asdecimal=False))
    event_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    event_type = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    master_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmEventMaster(Base):
    __tablename__ = 't_mt_vm_event_master'

    begin_date = Column(DateTime)
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    end_date = Column(DateTime)
    end_time = Column(String(8))
    event_desc = Column(String(200))
    event_name = Column(String(100))
    event_type = Column(Numeric(scale=0, asdecimal=False))
    master_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    start_time = Column(String(8))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    event_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmLock(Base):
    __tablename__ = 't_mt_vm_lock'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    effect_date = Column(DateTime)
    key_status = Column(Numeric(scale=0, asdecimal=False))
    lock_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    lock_key = Column(String(20))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmMaintenance(Base):
    __tablename__ = 't_mt_vm_maintenance'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    maintenance_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    operation_desc = Column(String(200))
    operation_type = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    uvp_uid = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmModel(Base):
    __tablename__ = 't_mt_vm_model'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    model_desc = Column(String(200))
    model_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    model_name = Column(String(50))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    allow_merge = Column(Numeric(scale=0, asdecimal=False))
    channel_layer_qty = Column(Numeric(scale=0, asdecimal=False))
    channel_per_layer = Column(String(100))
    channel_type = Column(Numeric(scale=0, asdecimal=False))
    coling_hdid = Column(Numeric(scale=0, asdecimal=False))
    company_init = Column(String(10))
    cooling_yn = Column(Numeric(scale=0, asdecimal=False))
    elevator_platform_hdid = Column(Numeric(scale=0, asdecimal=False))
    elevator_platform_yn = Column(Numeric(scale=0, asdecimal=False))
    hitting_hdid = Column(Numeric(scale=0, asdecimal=False))
    machine_view = Column(Numeric(scale=0, asdecimal=False))
    rfid_card = Column(Numeric(scale=0, asdecimal=False))
    screen_size = Column(Numeric(scale=0, asdecimal=False))
    screen_type = Column(Numeric(scale=0, asdecimal=False))
    shortcuts_qty = Column(Numeric(scale=0, asdecimal=False))
    temperature_handler_mode = Column(Numeric(scale=0, asdecimal=False))
    vend_out_architecture = Column(Numeric(scale=0, asdecimal=False))
    vend_out_type = Column(Numeric(scale=0, asdecimal=False))
    hitting_yn = Column(Numeric(asdecimal=False))
    temp_box_count = Column(Numeric(scale=0, asdecimal=False))
    temp_ctrl_desc = Column(String(200))


class TMtVmModelChannel(Base):
    __tablename__ = 't_mt_vm_model_channel'

    accept_width_max = Column(Numeric(scale=0, asdecimal=False))
    channel_code = Column(String(10))
    channel_height = Column(Numeric(scale=0, asdecimal=False))
    channel_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    channel_length = Column(Numeric(scale=0, asdecimal=False))
    channel_type = Column(Numeric(scale=0, asdecimal=False))
    channel_width = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    model_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    display_mode = Column(Numeric(scale=0, asdecimal=False))
    fixed_capacity = Column(Numeric(scale=0, asdecimal=False))
    is_fixed_capacity = Column(Numeric(scale=0, asdecimal=False))


class TMtVmPrice(Base):
    __tablename__ = 't_mt_vm_price'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    price_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    real_price = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmResource(Base):
    __tablename__ = 't_mt_vm_resource'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    delete_mark = Column(Numeric(scale=0, asdecimal=False))
    preview_urls = Column(String(300))
    resource_desc = Column(String(500))
    resource_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    resource_md5 = Column(String(32))
    resource_name = Column(String(50))
    resource_size = Column(Numeric(scale=0, asdecimal=False))
    resource_url = Column(String(100))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    resource_type = Column(Numeric(scale=0, asdecimal=False))


class TMtVmShortcut(Base):
    __tablename__ = 't_mt_vm_shortcuts'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    shortcuts_code = Column(String(5))
    shortcuts_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    bind_id = Column(Numeric(scale=0, asdecimal=False))
    bind_type = Column(Numeric(scale=0, asdecimal=False))


class TMtVmSkuSort(Base):
    __tablename__ = 't_mt_vm_sku_sort'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    sort = Column(Numeric(scale=0, asdecimal=False))
    sort_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmSkuSortNext(Base):
    __tablename__ = 't_mt_vm_sku_sort_next'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    sort = Column(Numeric(scale=0, asdecimal=False))
    sort_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmStrategy(Base):
    __tablename__ = 't_mt_vm_strategy'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    strategy_name = Column(String(100))
    sysn_mark = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    strategy_type = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(asdecimal=False), primary_key=True)


class TMtVmText(Base):
    __tablename__ = 't_mt_vm_text'

    begin_date = Column(DateTime)
    customer_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    end_date = Column(DateTime)
    text_contents = Column(String(2000))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmTheme(Base):
    __tablename__ = 't_mt_vm_theme'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    theme_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmThemeFormat(Base):
    __tablename__ = 't_mt_vm_theme_format'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    theme_format = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TMtVmVersion(Base):
    __tablename__ = 't_mt_vm_version'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    device_name = Column(String(50))
    device_version = Column(String(50))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    version_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    device_type = Column(Numeric(scale=0, asdecimal=False))


class TMtWarehouse(Base):
    __tablename__ = 't_mt_warehouse'

    contact_name = Column(String(20))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    dimensions = Column(String(20))
    longitude = Column(String(20))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    warehouse_address = Column(String(100))
    warehouse_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    warehouse_level = Column(Numeric(scale=0, asdecimal=False))
    warehouse_manager = Column(String(50))
    warehouse_name = Column(String(50))
    warehouse_phone = Column(String(20))
    warehouse_type = Column(String(1))
    warehouse_code = Column(String(9))


class TMtWarehouseArea(Base):
    __tablename__ = 't_mt_warehouse_area'

    area_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    warehouse_id = Column(Numeric(scale=0, asdecimal=False))
    wa_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)


class TProOrder(Base):
    __tablename__ = 't_pro_order'

    cost_amount = Column(Numeric(scale=0, asdecimal=False))
    cost_status = Column(Numeric(scale=0, asdecimal=False))
    cost_time = Column(DateTime)
    cost_type = Column(Numeric(scale=0, asdecimal=False))
    create_time = Column(DateTime)
    deal_seq = Column(String(50))
    order_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    seq = Column(String(50))
    total_amount = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    wechat_package = Column(String(50))
    wechat_user_id = Column(Numeric(scale=0, asdecimal=False))


class TProOrderGood(Base):
    __tablename__ = 't_pro_order_good'

    base_price = Column(Numeric(scale=0, asdecimal=False))
    channel_id = Column(Numeric(scale=0, asdecimal=False))
    extract_code = Column(String(8))
    good_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    notify_status = Column(Numeric(scale=0, asdecimal=False))
    notify_time = Column(DateTime)
    order_id = Column(Numeric(scale=0, asdecimal=False))
    real_price = Column(Numeric(scale=0, asdecimal=False))
    refund_seq = Column(String(50))
    refund_status = Column(Numeric(scale=0, asdecimal=False))
    refund_time = Column(DateTime)
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    valid_time = Column(String(12))
    vendout_status = Column(Numeric(scale=0, asdecimal=False))
    vendout_time = Column(DateTime)


class TReserveStatistic(Base):
    __tablename__ = 't_reserve_statistics'

    distribution_num = Column(Numeric(scale=0, asdecimal=False))
    pending_num = Column(Numeric(scale=0, asdecimal=False))
    reserve_statistics_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    statistics_date = Column(String(10))
    totalnum = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


t_t_sale_seq_factor = Table(
    't_sale_seq_factor', metadata,
    Column('ctime', DateTime),
    Column('host_name', String(20)),
    Column('sale_seq_factor_id', Numeric(scale=0, asdecimal=False))
)


class TSlOrderCallback(Base):
    __tablename__ = 't_sl_order_callback'

    callback_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    callback_status = Column(Numeric(scale=0, asdecimal=False))
    callback_time = Column(DateTime)
    order_id = Column(Numeric(scale=0, asdecimal=False))


class TSlOrderCost(Base):
    __tablename__ = 't_sl_order_cost'

    cost_account = Column(String(50))
    cost_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    cost_price = Column(Numeric(scale=0, asdecimal=False))
    cost_status = Column(Numeric(scale=0, asdecimal=False))
    cost_time = Column(DateTime)
    cost_type = Column(Numeric(scale=0, asdecimal=False))
    deal_seq = Column(String(50))
    order_id = Column(Numeric(scale=0, asdecimal=False))


class TSlOrderGiro(Base):
    __tablename__ = 't_sl_order_giro'

    account_name = Column(String(20))
    account_no = Column(String(50))
    account_type = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    giro_month = Column(String(7))
    giro_seq = Column(String(50))
    giro_status = Column(Numeric(scale=0, asdecimal=False))
    giro_time = Column(DateTime)
    order_giro_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    s_user_id = Column(Numeric(scale=0, asdecimal=False))
    transfer_amount = Column(Numeric(scale=0, asdecimal=False))


class TSlOrderMaster(Base):
    __tablename__ = 't_sl_order_master'

    company_id = Column(Numeric(scale=0, asdecimal=False))
    order_desc = Column(String(200))
    order_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    order_price = Column(Numeric(scale=0, asdecimal=False))
    order_seq = Column(String(50), nullable=False)
    order_time = Column(DateTime)
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    spare = Column(String(50))
    vm_id = Column(Numeric(scale=0, asdecimal=False))


class TSlOrderNotify(Base):
    __tablename__ = 't_sl_order_notify'

    customer_public_id = Column(String(20))
    notify_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    notify_status = Column(Numeric(scale=0, asdecimal=False))
    notify_time = Column(DateTime)
    notify_url = Column(String(200))
    order_id = Column(Numeric(scale=0, asdecimal=False))


class TSlOrderRefund(Base):
    __tablename__ = 't_sl_order_refund'

    account = Column(String(50))
    amount = Column(Numeric(scale=0, asdecimal=False))
    ctor = Column(Numeric(scale=0, asdecimal=False))
    refund_desc = Column(String(200))
    refund_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refund_seq = Column(String(50), nullable=False)
    refund_status = Column(Numeric(scale=0, asdecimal=False))
    refund_time = Column(DateTime)
    spare = Column(String(50))
    type = Column(Numeric(scale=0, asdecimal=False))
    order_id = Column(Numeric(scale=0, asdecimal=False))


class TSlOrderSale(Base):
    __tablename__ = 't_sl_order_sale'

    sale_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sale_seq = Column(String(50), nullable=False)
    sale_desc = Column(String(200))
    sale_status = Column(Numeric(scale=0, asdecimal=False))
    sale_time = Column(DateTime)
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    vm_channel_id = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    sku_name = Column(String(50))
    cost_time = Column(DateTime)
    cost_status = Column(Numeric(scale=0, asdecimal=False))
    out_status = Column(Numeric(scale=0, asdecimal=False))
    out_time = Column(DateTime)
    pay_account = Column(String(50))
    pay_amount = Column(Numeric(scale=0, asdecimal=False))
    pay_type = Column(Numeric(scale=0, asdecimal=False))
    real_price = Column(Numeric(scale=0, asdecimal=False))
    company_id = Column(Numeric(scale=0, asdecimal=False))
    ctor = Column(Numeric(scale=0, asdecimal=False))
    deal_seq = Column(String(50))
    notify_status = Column(Numeric(scale=0, asdecimal=False))
    notify_time = Column(DateTime)
    sync_mark = Column(Numeric(asdecimal=False))
    sync_time = Column(DateTime)
    spare = Column(String(50))


class TSlOrderVendout(Base):
    __tablename__ = 't_sl_order_vendout'

    order_id = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    vendout_channel_id = Column(Numeric(scale=0, asdecimal=False))
    vendout_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    vendout_status = Column(Numeric(scale=0, asdecimal=False))
    vendout_time = Column(DateTime)


class TStVmChannel(Base):
    __tablename__ = 't_st_vm_channel'

    channel_code = Column(String(10))
    channel_height = Column(Numeric(scale=0, asdecimal=False))
    channel_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    channel_long = Column(Numeric(scale=0, asdecimal=False))
    channel_width = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    inner_code = Column(String(20))
    max_capacity = Column(Numeric(scale=0, asdecimal=False))
    merge_qty = Column(Numeric(scale=0, asdecimal=False))
    pc_type = Column(Numeric(scale=0, asdecimal=False))
    remarks = Column(String(200))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))
    accept_width_max = Column(Numeric(9, 0, asdecimal=False))
    display_mode = Column(Numeric(9, 0, asdecimal=False))
    fixed_capacity = Column(Numeric(9, 0, asdecimal=False))
    is_fixed_capacity = Column(Numeric(9, 0, asdecimal=False))
    merge_pid = Column(Numeric(9, 0, asdecimal=False))


class TStVmEnergySave(Base):
    __tablename__ = 't_st_vm_energy_save'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    customer_id = Column(Numeric(scale=0, asdecimal=False))
    end_time = Column(String(8))
    energy_save_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    energy_save_type = Column(Numeric(scale=0, asdecimal=False))
    remark = Column(String(200))
    start_time = Column(String(8))
    target_value = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))
    temp_box_no = Column(Numeric(scale=0, asdecimal=False))


class TStVmEvent(Base):
    __tablename__ = 't_st_vm_event'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    discount_type = Column(Numeric(scale=0, asdecimal=False))
    discount_value = Column(Numeric(scale=0, asdecimal=False))
    event_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    event_type = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))


class TStVmPrice(Base):
    __tablename__ = 't_st_vm_price'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    price_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    real_price = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))


class TStVmShortcut(Base):
    __tablename__ = 't_st_vm_shortcuts'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    shortcuts_code = Column(String(5))
    shortcuts_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))
    bind_id = Column(Numeric(scale=0, asdecimal=False))
    bind_type = Column(Numeric(scale=0, asdecimal=False))


class TStVmSkuSort(Base):
    __tablename__ = 't_st_vm_sku_sort'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    sort = Column(Numeric(scale=0, asdecimal=False))
    sort_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))


class TStVmStrategy(Base):
    __tablename__ = 't_st_vm_strategy'

    company_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    strategy_name = Column(String(100))
    strategy_type = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    strategy_desc = Column(String(200))
    model_id = Column(Numeric(9, 0, asdecimal=False))


class TStVmText(Base):
    __tablename__ = 't_st_vm_text'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    end_time = Column(String(8))
    start_time = Column(String(8))
    st_text_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    text_contents = Column(String(2000))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    strategy_id = Column(Numeric(scale=0, asdecimal=False))


class TSysDictionary(Base):
    __tablename__ = 't_sys_dictionary'

    dictionary_code = Column(String(50))
    dictionary_desc = Column(String(200))
    dictionary_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    dictionary_name = Column(String(50))
    dictionary_state = Column(Numeric(scale=0, asdecimal=False))
    type_info_id = Column(Numeric(scale=0, asdecimal=False))


class TSysElement(Base):
    __tablename__ = 't_sys_element'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    element_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    element_type = Column(String(50))
    element_url = Column(String(100))
    p_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    element_code = Column(String(50))
    element_index = Column(Numeric(asdecimal=False))
    element_name = Column(String(50))
    element_module = Column(Numeric(scale=0, asdecimal=False))


t_t_sys_element_bak = Table(
    't_sys_element_bak', metadata,
    Column('ctime', DateTime),
    Column('ctor', Numeric(scale=0, asdecimal=False)),
    Column('element_code', String(50)),
    Column('element_id', Numeric(scale=0, asdecimal=False), nullable=False),
    Column('element_index', Numeric(scale=0, asdecimal=False)),
    Column('element_module', Numeric(scale=0, asdecimal=False)),
    Column('element_name', String(50)),
    Column('element_type', String(50)),
    Column('element_url', String(100)),
    Column('p_id', Numeric(scale=0, asdecimal=False)),
    Column('utime', DateTime),
    Column('utor', Numeric(scale=0, asdecimal=False))
)


class TSysLog(Base):
    __tablename__ = 't_sys_log'

    log_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    log_operation = Column(String(500))
    log_time = Column(DateTime)
    module_id = Column(Numeric(scale=0, asdecimal=False))
    user_id = Column(Numeric(scale=0, asdecimal=False))
    log_desc = Column(String(2000))


class TSysRole(Base):
    __tablename__ = 't_sys_role'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    company_id = Column(Numeric(scale=0, asdecimal=False))
    role_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    role_level = Column(Numeric(scale=0, asdecimal=False))
    role_name = Column(String(50))
    role_type = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    role_desc = Column(String(200))


class TSysRoleElement(Base):
    __tablename__ = 't_sys_role_element'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    element_id = Column(Numeric(scale=0, asdecimal=False))
    re_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    role_id = Column(Numeric(scale=0, asdecimal=False))


class TSysSetting(Base):
    __tablename__ = 't_sys_settings'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    key = Column(String(32))
    name = Column(String(256))
    pid = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    value = Column(String(256))


class TSysTypeInfo(Base):
    __tablename__ = 't_sys_type_info'

    type_code = Column(String(50))
    type_desc = Column(String(200))
    type_info_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    type_name = Column(String(50))


class TSysUser(Base):
    __tablename__ = 't_sys_user'

    company_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    delete_mark = Column(Numeric(scale=0, asdecimal=False))
    fail_count = Column(Numeric(scale=0, asdecimal=False))
    lock_mark = Column(Numeric(scale=0, asdecimal=False), server_default=text("0"))
    login_time = Column(DateTime, server_default=text("sysdate"))
    user_account = Column(String(32))
    user_email = Column(String(50))
    user_gender = Column(Numeric(scale=0, asdecimal=False))
    user_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    user_name = Column(String(20))
    user_password = Column(String(32))
    user_phone = Column(String(20))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))


class TSysUserBind(Base):
    __tablename__ = 't_sys_user_bind'

    bind_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    bind_type = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    outer_id = Column(String(50))
    user_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))


class TSysUserRole(Base):
    __tablename__ = 't_sys_user_role'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    role_id = Column(Numeric(scale=0, asdecimal=False))
    ur_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    user_id = Column(Numeric(scale=0, asdecimal=False))


class TTaskPickupHi(Base):
    __tablename__ = 't_task_pickup_his'

    pickup_count = Column(Numeric(scale=0, asdecimal=False))
    pickup_sku_id = Column(Numeric(scale=0, asdecimal=False))
    pickup_time = Column(DateTime)
    pickup_user_id = Column(Numeric(scale=0, asdecimal=False))
    task_pickup_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)


class TTaskVm(Base):
    __tablename__ = 't_task_vm'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    finish_time = Column(DateTime)
    owner = Column(Numeric(scale=0, asdecimal=False))
    task_level = Column(Numeric(scale=0, asdecimal=False))
    task_remarks = Column(String(2000))
    task_time = Column(DateTime)
    task_title = Column(String(200))
    task_type = Column(Numeric(scale=0, asdecimal=False))
    task_vm_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    task_vm_status = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    company_id = Column(Numeric(asdecimal=False))
    already_pickup = Column(Numeric(scale=0, asdecimal=False))


class TTaskVmChannel(Base):
    __tablename__ = 't_task_vm_channel'

    channel_id = Column(Numeric(scale=0, asdecimal=False))
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    sku_count = Column(Numeric(scale=0, asdecimal=False))
    sku_id = Column(Numeric(scale=0, asdecimal=False))
    task_type = Column(Numeric(scale=0, asdecimal=False))
    task_vm_channel_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    task_vm_id = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    task_remarks = Column(String(200))
    after_delivery_stock = Column(Numeric(scale=0, asdecimal=False))
    before_delivery_stock = Column(Numeric(scale=0, asdecimal=False))


class TVmOperationHi(Base):
    __tablename__ = 't_vm_operation_his'

    client_time = Column(DateTime)
    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    vm_door_status = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    vm_operation_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)


class TVmStatu(Base):
    __tablename__ = 't_vm_status'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    utime = Column(DateTime)
    utor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    vm_status_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    temp_value = Column(String(500))
    vm_status = Column(Numeric(scale=0, asdecimal=False))
    vm_status_datail = Column(String(2000))
    vm_time = Column(DateTime)
    vm_door_status = Column(Numeric(scale=0, asdecimal=False))


class TVmStatusHi(Base):
    __tablename__ = 't_vm_status_his'

    ctime = Column(DateTime)
    ctor = Column(Numeric(scale=0, asdecimal=False))
    vm_id = Column(Numeric(scale=0, asdecimal=False))
    vm_status_his_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    temp_value = Column(String(500))
    vm_status = Column(Numeric(scale=0, asdecimal=False))
    vm_status_datail = Column(String(2000))
    vm_time = Column(DateTime)
    door_status = Column(Numeric(scale=0, asdecimal=False))


class TWechatUser(Base):
    __tablename__ = 't_wechat_user'

    nick_name = Column(String(32))
    open_id = Column(String(50), nullable=False)
    phone = Column(String(15))
    photo = Column(String(500))
    user_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)


class TWechatUserHistory(Base):
    __tablename__ = 't_wechat_user_history'

    history_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    user_id = Column(Numeric(scale=0, asdecimal=False))
    use_date = Column(DateTime)
    vm_id = Column(Numeric(scale=0, asdecimal=False))
