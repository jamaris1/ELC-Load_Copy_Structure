merge ='''
INSERT into XFR_MERCH_TRANSFERS_ACTIVITY
    (
    "BUSINESS_UNIT_ID" , 
    "TRANSFER_ID" , 
    "TRANSFER_OCCURENCE_TYPE" , 
    "TRANSFER_ORIGIN_NAME" , 
    "FROM_SITE_ID" , 
    "TO_SITE_ID" , 
    "TRANSFER_TYPE" , 
    "DISTRIBUTION_ID" , 
    "ACTIVITY_TYPE" , 
    "CREATION_DATE" , 
    "STATUS" , 
    "PROCESSED_DATE", 
    "USERNAME" , 
    "FROM_BUSINESS_UNIT_ID", 
    "TO_BUSINESS_UNIT_ID", 
    "WMS_FLAG", 
    "WMS_PROCESSED_DATE"
    )
        SELECT
        src.$1,
        src.$2,
        src.$3,
        src.$4,
        src.$5,
        src.$6,
        src.$7,
        src.$8,
        src.$9,
        src.$10,
        src.$11,
        src.$12,
        src.$13,
        src.$14,
        src.$15,
        src.$16,
        src.$17
        FROM @{v_sf_stage}/{file}( FILE_FORMAT => csv_file_format) src; '''