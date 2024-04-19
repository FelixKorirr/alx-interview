#!/usr/bin/python3
"""Solves lock boxes puzzle """


def look_for_next_opened_box(opened):
    """Looks for the next opened box"""
    for indx, box in opened.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    a = {}
    while True:
        if len(a) == 0:
            a[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_for_next_opened_box(a)
        if keys:
            for k in keys:
                try:
                    if a.get(k) and a.get(k).get('status') \
                       == 'opened/checked':
                        continue
                    a[k] = {
                        'status': 'opened',
                        'keys': boxes[k]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in a.values()]:
            continue
        elif len(a) == len(boxes):
            break
        else:
            return False

    return len(a) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
