merge='''
                INSERT INTO XFR_MERCH_IRI_POS_TRANSFERS
                 (
                    "JOB_ID" , 
                    "BUSINESS_UNIT_ID" , 
                    "TRANSFER_ID" , 
                    "TRANSFER_OCCURENCE_TYPE" , 
                    "LINE_NO" , 
                    "PRGID" , 
                    "TRANSFER_TYPE" , 
                    "TRANSFER_DATE" , 
                    "REQUEST_ID" , 
                    "FROM_SITE" , 
                    "TO_SITE" , 
                    "BAR_CODE_BUS_UNIT_ID" , 
                    "BAR_CODE_SUB_TYPE" , 
                    "BAR_CODE_ID" , 
                    "STYLE_ID" , 
                    "COLOR_ID" , 
                    "DIMENSION_ID", 
                    "VALID_DIMENSION_ID" , 
                    "SIZE_ID" , 
                    "VALID_SIZE_ID" , 
                    "ITEM_QTY" , 
                    "VALID_IND" , 
                    "STATUS" , 
                    "SITE_ID" , 
                    "VALID_HEADER" , 
                    "VALID_DETAIL" , 
                    "DATE_CREATED" , 
                    "REASON_ID" , 
                    "TRANSFER_ORIGIN_NAME" , 
                    "FROM_SITE_RETAIL_VALUE" , 
                    "TO_SITE_RETAIL_VALUE", 
                    "UNIT_COST" , 
                    "EXPENSE_TRANSFER_ID" , 
                    "REJ_RPT_PRINTED_IND" , 
                    "REJECTED_ID" , 
                    "REASON_SUB_TYPE" , 
                    "PROCESS_DATE_CREATED" , 
                    "PROCESS_STATUS" , 
                    "PROCESS_DATE_TIME" , 
                    "RICHTER_VERSION_ID" , 
                    "POS_VERSION_ID" , 
                    "CONTROL_NO" , 
                    "USER_IN_DATE" , 
                    "USER_TRACE_ID" , 
                    "USER_ID" , 
                    "RIDE_OUT_DATE" , 
                    "RIDE_ERROR_CODE" , 
                    "SEVERITY_CODE" , 
                    "INVENTORY_ADJUST_ID" , 
                    "FROM_BUSINESS_UNIT_ID" , 
                    "TO_BUSINESS_UNIT_ID" , 
                    "CANCEL_IND" , 
                    "POS_TRANSFER_ID" , 
                    "WEB_TRACKING_NUMBER" , 
                    "TRANSACTION_NO" , 
                    "TRANSFER_COMPLETE_IND" , 
                    "ACTIVATION_DATE" , 
                    "COMMENTS" , 
                    "CARTON_ID" , 
                    "WEB_ORDER_ID" , 
                    "RMA_CODE"
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
                 src.$57,
                 src.$58,
                 src.$59, 
                 src.$60,
                 src.$61
                 FROM @{v_sf_stage}/{file}( FILE_FORMAT => csv_file_format) src; '''