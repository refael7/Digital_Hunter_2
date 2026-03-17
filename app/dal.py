from app.config.connection import client
from maps_data.DigitalHunter_map import plot_map_with_geometry




def traffic_alert():
    sql = """
       
            SELECT entity_id, target_name, priority_level, movement_distance_km
            FROM targets
            WHERE priority_level IN(1,2) AND movement_distance>5;
            """.strip()

    return client.fetch_all(sql)

def analysis_of_collection_sources():
    sql ="""
    
            SELECT signal_type,COUNT(*) as count_all
            FROM intel_signals
            GROUP BY signal_type
            ORDER BY count_all DESC
    
            """.strip()
    return client.fetch_all(sql)



def finding_new_targets():
    sql= """
   
    SELECT entity_id ,COUNT(*) as count_all
    FROM  intel_signals
    GROUP BY entity_id,priority_level
    having priority_level = 99
    or entity_id like "%UNKNOWN%"
    ORDER BY count_all DESC
    LIMIT 3
        """.strip()

    return client.fetch_all(sql)




def identifying_awakened_sleeping_cells():

    sql= """
    SELECT day_table.entity_id from(
    SELECT entity_id 
    FROM intel_signals
    where hour(timestamp) between 8 and 20
    group by entity_id 
    having sum(distance_from_last)=0)
    as dey_table
    inner join(
    select entity_id 
    from intel_signals
    where hour(timestamp) not between 8 and 20
    group by entity_id 
    having sum(distance_from_last)>10
    as night_table

        """.strip()

    return client.fetch_all(sql)


def visualization_of_a_target_trajectory(entity_id):
     result = []
     client("""
     select *
     from intel_signals
     where entity_id  = %s
     """,[entity_id])
     f=client.fetch_all()
     for i in f:
         result.append(i)
     plot_map_with_geometry(result)



