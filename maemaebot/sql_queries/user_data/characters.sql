begin;

create table if not exists
    campaigns.characters
(
    user_id bigint,
    campaign_id bigint,
    character_id int,
    channel_id bigint,
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
    active boolean,
    "default" boolean,
    created_time timestamp default now()
);

create index if not exists
    characters_user_id_idx
on
    campaigns.characters(
        user_id,
        character_id
    )
;
create index if not exists
    characters_campaign_idx
on
    users.characters(
        user_id,
        campaign_id
    )
;

commit;