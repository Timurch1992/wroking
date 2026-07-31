# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: PetCare
def get_next_recommendation(pet, last_log):
    """Recommend next action based on pet state and recent logs."""
    recs = []
    if pet.name:
        recs.append(f"Hello {pet.name}! 🐾")
    # Feeding schedule (every 12h)
    if last_log.get("feeding_time"):
        hours_since_feed = (datetime.now() - datetime.fromisoformat(last_log["feeding_time"])).total_seconds() / 3600
        if hours_since_feed >= 10:
            recs.append(f"💧 {pet.name} hasn't eaten in {hours_since_feed:.0f}h — offer food soon!")
    # Health check (every 8h)
    if last_log.get("health_check"):
        hours_since_health = (datetime.now() - datetime.fromisoformat(last_log["health_check"])).total_seconds() / 3600
        if hours_since_health >= 7:
            recs.append(f"🩺 Time for a health check on {pet.name}!")
    # Walk schedule (every 24h)
    if last_log.get("walk_time"):
        hours_since_walk = (datetime.now() - datetime.fromisoformat(last_log["walk_time"])).total_seconds() / 3600
        if hours_since_walk >= 22:
            recs.append(f"🌳 {pet.name} needs a walk — it's been {hours_since_walk:.0f}h!")
    # Hydration (every 12h)
    if last_log.get("water_time"):
        hours_since_water = (datetime.now() - datetime.fromisoformat(last_log["water_time"])).total_seconds() / 3600
        if hours_since_water >= 10:
            recs.append(f"💧 Offer water to {pet.name} — it's been {hours_since_water:.0f}h!")
    # Mood check (every 24h)
    if last_log.get("mood_check"):
        hours_since_mood = (datetime.now() - datetime.fromisoformat(last_log["mood_check"])).total_seconds() / 3600
        if hours_since_mood >= 22:
            recs.append(f"😊 Check in on {pet.name}'s mood!")
    # Weight check (weekly)
    if last_log.get("weight_check"):
        days_since_weight = (datetime.now() - datetime.fromisoformat(last_log["weight_check"])).total_seconds() / 86400
        if days_since_weight >= 7:
            recs.append(f"⚖️ Weigh {pet.name} — it's been {days_since_weight:.1f} days!")
    return "\n".join(recs) if recs else "🌟 All looks good! No urgent tasks right now."
