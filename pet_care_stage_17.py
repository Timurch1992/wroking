# === Stage 17: Добавь группировку записей по категориям ===
# Project: PetCare
from collections import defaultdict, deque
from datetime import timedelta

def group_activities_by_category(activities):
    grouped = defaultdict(list)
    for act in activities:
        cat = act.get('category', 'other')
        grouped[cat].append(act)
    
    sorted_groups = {k: sorted(v, key=lambda x: x['timestamp'], reverse=True) 
                     for k, v in grouped.items()}
    return dict(sorted_groups)

def get_summary_stats(grouped_activities):
    stats = {}
    total_count = sum(len(v) for v in grouped_activities.values())
    
    if not grouped_activities or total_count == 0:
        return {'total': 0, 'categories': {}}
        
    category_counts = [len(v) for v in grouped_activities.values()]
    stats['total'] = total_count
    
    top_categories = sorted(grouped_activities.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    stats['top_categories'] = [{'name': name, 'count': count} for name, items in top_categories]
    
    return stats

def filter_by_date_range(activities, start_time=None, end_time=None):
    filtered = []
    for act in activities:
        ts = act.get('timestamp')
        if start_time and ts < start_time:
            continue
        if end_time and ts > end_time:
            continue
        filtered.append(act)
    return filtered

def get_recent_activities(activities, count=5):
    sorted_acts = sorted(activities, key=lambda x: x.get('timestamp', ''), reverse=True)[:count]
    return sorted_acts
