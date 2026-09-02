# === Stage 43: Добавь пагинацию длинных списков ===
# Project: PetCare
def paginate(items, page_size=10):
    """Compact paginator: yields (page_index, page_items) tuples."""
    for i in range(0, len(items), page_size):
        yield i // page_size, items[i:i+page_size]
