from app.models.equipment import Equipment
from app.models.equipment_spec import Equipment_Spec
from app.models.equipment_distance import Equipment_Distance

# function to match a join the 3 equipment tables 
def build_equipment_record(club, spec, distance):
  equipment_list = []
  for c in club:
    club_dict = {
      'club': Equipment(equipment_id=c['equipment_id'], person_id=c['person_id'], ss_id=c['ss_id'], catagory=c['catagory'], name=c['name'], short_name=c['short_name'], make=c['make'], model=c['model'], year=c['year'], active=c['active']).as_dict()
    }

    # get equipment id and filter spec and distance on that id
    e_id = c['equipment_id']
    s = [s for s in spec if s['equipment_id'] == e_id][0]
    club_dict['spec'] = Equipment_Spec(equipment_spec_id=s['equipment_spec_id'], equipment_id=s['equipment_id'], loft=s['loft'], lie=s['lie'], club_length=s['club_length'], wieght=s['wieght'], club_head=s['club_head'], head_weight=s['head_weight'], club_offset=s['club_offset'], bounce=s['bounce'], swing_weight=s['swing_weight'], shaft=s['shaft'], shaft_flex=s['shaft_flex'], shaft_weight=s['shaft_weight'], grip=s['grip'], grip_core_dia=s['grip_core_dia'], grip_weight=s['grip_weight'], grip_size=s['grip_size']).as_dict()
    
    d = [d for d in distance if d['equipment_id'] == e_id][0]
    club_dict['distance'] = Equipment_Distance(equipment_distance_id=d['equipment_distance_id'], equipment_id=d['equipment_id'], manual_max_distance=d['manual_max_distance'], manual_stock_distance=d['manual_stock_distance'], manual_knockdown_distance=d['manual_knockdown_distance'], manual_shoulder_distance=d['manual_shoulder_distance'], manual_hip_distance=d['manual_hip_distance'], manual_knee_distance=d['manual_knee_distance'], manual_dispersion=d['manual_dispersion'], calc_max_distance=d['calc_max_distance'], calc_stock_distance=d['calc_stock_distance'], calc_knockdown_distance=d['calc_knockdown_distance'], calc_shoulder_distance=d['calc_shoulder_distance'], calc_hip_distance=d['calc_hip_distance'], calc_knee_distance=d['calc_knee_distance'], calc_dispersion=d['calc_dispersion']).as_dict()

    # append to list
    equipment_list.append(club_dict)

  return equipment_list
