merge ='''
                INSERT INTO XFR_MERCH_IRO_POS_REQUESTS
                 (
                        "BUSINESS_UNIT_ID" , 
                        "FROM_SITE_ID" , 
                        "TRANSFER_ID" , 
                        "DISTRIBUTION_ID" , 
                        "LINE_NO" , 
                        "BAR_CODE_SUB_TYPE" , 
                        "BAR_CODE_ID" , 
                        "STYLE_ID" , 
                        "COLOR_ID" , 
                        "DIMENSION_ID" , 
                        "SIZE_ID" , 
                        "ITEM_QTY" , 
                        "TO_BUSINESS_UNIT_ID" , 
                        "TO_SITE_ID" , 
                        "TRANSFER_DATE" , 
                        "REASON_SUB_TYPE" , 
                        "REASON_ID" , 
                        "REQUEST_TRANSFER_ID" , 
                        "TO_SITE_RETAIL_VALUE" , 
                        "FROM_SITE_RETAIL_VALUE" , 
                        "UNIT_COST" , 
                        "REMARKS" , 
                        "JOB_ID" , 
                        "RICHTER_VERSION_ID" , 
                        "POS_VERSION_ID" , 
                        "CONTROL_NO" , 
                        "RIDE_IN_DATE" , 
                        "RIDE_TRACE_ID" , 
                        "USER_ID" , 
                        "RIDE_OUT_DATE" , 
                        "RIDE_ERROR_CODE" , 
                        "ACTIVITY_TYPE" , 
                        "DOWNLOAD_TYPE" , 
                        "PROCESS_DATE_CREATED" , 
                        "PROCESS_STATUS" , 
                        "PROCESS_DATE_TIME" , 
                        "SALES_ORDER_ID" , 
                        "WEB_CUSTOMER_ID" , 
                        "SHIP_COMPLETE_IND" , 
                        "RUSH_SHIPPING_IND" , 
                        "FIRST_NAME" , 
                        "INITIALS" , 
                        "LAST_NAME" , 
                        "SALUTATION" , 
                        "ADDRESS_1" , 
                        "ADDRESS_2" , 
                        "ADDRESS_3" , 
                        "ADDRESS_4" , 
                        "CITY" , 
                        "STATE_ID" , 
                        "ZIP_CODE" , 
                        "COUNTRY_ID" , 
                        "HOME_PHONE" , 
                        "WORK_PHONE" , 
                        "CELL_PHONE" , 
                        "SHIPPING_INFO" , 
                        "COMMENTS" 
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
                 src.$17,
                 src.$18,
                 src.$19,
                 src.$20,
                 src.$21,
                 src.$22,
                 src.$23,
                 src.$24,
                 src.$25,
                 src.$26,
                 src.$27,
                 src.$28,
                 src.$29,
                 src.$30,
                 src.$31,
                 src.$32,
                 src.$33,
                 src.$34,
                 src.$35,
                 src.$36,
                 src.$37,
                 src.$38,
                 src.$39,
                 src.$40,
                 src.$41,
                 src.$42,
                 src.$43,
                 src.$44,
                 src.$45,
                 src.$46,
                 src.$47,
                 src.$48,
                 src.$49,
                 src.$50,
                 src.$51,
                 src.$52,
                 src.$53,
                 src.$54,
                 src.$55,
                 src.$56,
                 src.$57
                 FROM @{v_sf_stage}/{file}( FILE_FORMAT => csv_file_format) src; '''