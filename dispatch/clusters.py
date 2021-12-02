hosts = [

    # shi:
    "shi-c1-p1", "shi-c1-p2", "shi-c1-p3", "shi-c1-p4", "shi-c1-p5", "shi-c1-p6",
    "shi-c2-p1", "shi-c2-p2", "shi-c2-p3", "shi-c2-p4", "shi-c2-p5", "shi-c2-p6",
    "shi-r1-p1", "shi-r1-p2", "shi-r1-p3", "shi-r1-p4", "shi-r1-p5", "shi-r1-p6", "shi-r1-p7", "shi-r1-p8",
    "shi-r2-p1", "shi-r2-p2", "shi-r2-p3", "shi-r2-p4", "shi-r2-p5", "shi-r2-p6", "shi-r2-p7", "shi-r2-p8",
    "shi-r3-p1", "shi-r3-p2", "shi-r3-p3", "shi-r3-p4", "shi-r3-p5", "shi-r3-p6", "shi-r3-p7", "shi-r3-p8",
    "shi-r4-p1", "shi-r4-p2", "shi-r4-p3", "shi-r4-p4", "shi-r4-p5", "shi-r4-p6", "shi-r4-p7", "shi-r4-p8",
    "shi-r5-p1", "shi-r5-p2", "shi-r5-p3", "shi-r5-p4", "shi-r5-p5", "shi-r5-p6", "shi-r5-p7", "shi-r5-p8",
    "shi-r6-p1", "shi-r6-p2", "shi-r6-p3", "shi-r6-p4", "shi-r6-p5", "shi-r6-p6", "shi-r6-p7", "shi-r6-p8",
    "shi-r7-p1", "shi-r7-p2", "shi-r7-p3", "shi-r7-p4", "shi-r7-p5", "shi-r7-p6", "shi-r7-p7", "shi-r7-p8",
    "shi-r8-p1", "shi-r8-p2", "shi-r8-p3", "shi-r8-p4", "shi-r8-p5", "shi-r8-p6", "shi-r8-p7", "shi-r8-p8",
    "shi-r9-p1", "shi-r9-p2", "shi-r9-p3", "shi-r9-p4", "shi-r9-p5", "shi-r9-p6", "shi-r9-p7", "shi-r9-p8",
    "shi-r10-p1", "shi-r10-p2", "shi-r10-p3", "shi-r10-p4", "shi-r10-p5", "shi-r10-p6", "shi-r10-p7", "shi-r10-p8",
    "shi-r11-p1", "shi-r11-p2", "shi-r11-p3", "shi-r11-p4", "shi-r11-p5", "shi-r11-p6", "shi-r11-p7", "shi-r11-p8",
    "shi-r12-p1", "shi-r12-p2", "shi-r12-p3", "shi-r12-p4", "shi-r12-p5", "shi-r12-p6", "shi-r12-p7", "shi-r12-p8",


    # fu
    "fu-c1-p1", "fu-c1-p2", "fu-c1-p3",
    "fu-c2-p1", "fu-c2-p2", "fu-c2-p3", "fu-c2-p4", "fu-c2-p5",
    "fu-c3-p1", "fu-c3-p2", "fu-c3-p3", "fu-c3-p4", "fu-c3-p5", "fu-c3-p6",
    "fu-c4-p1", "fu-c4-p2", "fu-c4-p3", "fu-c4-p4", "fu-c4-p5",
    "fu-r1-p1", "fu-r1-p2", "fu-r1-p3", "fu-r1-p4", "fu-r1-p5", "fu-r1-p6", "fu-r1-p7", "fu-r1-p8",
    "fu-r2-p1", "fu-r2-p2", "fu-r2-p3", "fu-r2-p4", "fu-r2-p5", "fu-r2-p6", "fu-r2-p7", "fu-r2-p8",
    "fu-r3-p1", "fu-r3-p2", "fu-r3-p3", "fu-r3-p4", "fu-r3-p5", "fu-r3-p6", "fu-r3-p7", "fu-r3-p8",
    "fu-r4-p1", "fu-r4-p2", "fu-r4-p3", "fu-r4-p4", "fu-r4-p5", "fu-r4-p6", "fu-r4-p7", "fu-r4-p8",
    "fu-r5-p1", "fu-r5-p2", "fu-r5-p3", "fu-r5-p4", "fu-r5-p5", "fu-r5-p6", "fu-r5-p7", "fu-r5-p8",
    "fu-r6-p1", "fu-r6-p2", "fu-r6-p3", "fu-r6-p4", "fu-r6-p5", "fu-r6-p6", "fu-r6-p7", "fu-r6-p8",
    "fu-r7-p1", "fu-r7-p2", "fu-r7-p3", "fu-r7-p4", "fu-r7-p5", "fu-r7-p6", "fu-r7-p7", "fu-r7-p8",
    "fu-r8-p1", "fu-r8-p2", "fu-r8-p3", "fu-r8-p4", "fu-r8-p5", "fu-r8-p6", "fu-r8-p7", "fu-r8-p8",
    "fu-r9-p1", "fu-r9-p2", "fu-r9-p3", "fu-r9-p4", "fu-r9-p5", "fu-r9-p6", "fu-r9-p7", "fu-r9-p8",
    "fu-r10-p1", "fu-r10-p2", "fu-r10-p3", "fu-r10-p4", "fu-r10-p5", "fu-r10-p6", "fu-r10-p7", "fu-r10-p8",

    # mi:
    # TODO

]


def get_hosts(cluster: str):
    return [l for l in hosts if l.startswith(cluster)]


def get_hosts_from_regex(regex: str):
    # TODO
    return None
