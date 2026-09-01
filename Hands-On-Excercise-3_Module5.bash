read -r line < "Hands-On-Excercise-3_Module5SecretKey.txt"
curl -s -H "X-Api-Key: line" -H "mediaType: application/vnd.api+json" https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny | jq > out.json
