read -r line < "Hands-On-Excercise-3_Module5SecretKey.txt"
curl -s -H "X-Api-Key: line" -H "mediaType: application/vnd.api+json" https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance | jq > out2.json
