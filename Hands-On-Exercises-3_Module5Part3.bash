read -r line < "Hands-On-Excercise-3_Module5SecretKey.txt"
curl -s -H "X-Api-Key: line" -H "mediaType: application/vnd.api+json" https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/gas_held_by_public_daily_activity | jq > out3.json
