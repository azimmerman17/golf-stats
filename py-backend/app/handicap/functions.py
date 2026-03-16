# function to translate GHIN record to internal DB record
def create_record(data, id):
  return {
    'handicap_history_id': data['ID'],
    'ghin_number': data['GHINNumber'],
    'person_id': id,
    'assoc': data['AssociationName'],
    'club': data['ClubName'].replace("'", ""),
    'hard_soft_cap': data['Hard_Soft_Cap'],
    'hard_cap': data['Hard_Cap'],
    'soft_cap': data['Soft_Cap'],
    'rev_date': data['RevDate'],
    'hi_displsy': data['Display'],
    'hi_value': float(data['Value']),
    'low_hi_displsy': data['LowHIDisplay'],
    'low_hi_value': float(data['LowHI'])
  }

 