begin;

create table if not exists
    campaigns.npcs
(
    user_id bigint,
    campaign_id bigint,
    channel_id bigint,
    faction_id int,
    character_id int,
    character_username text,
    avatar_url text,
    profile_url text,
    "money" bigint,
    total_weight int,
    exp bigint,
    char_lvl int,
    hp int,
    str int,
    dex int,
    con int,
    wis int,
    "int" int,
    cha int,
    attacks text[],
    attributes text[].
    items text[],
    hostile_to text[],
    created_time timestamp default now()
);

create index if not exists
    npc_campaign_idx
on
    users.characters(
        character_id,
        campaign_id
    )
;

commit;