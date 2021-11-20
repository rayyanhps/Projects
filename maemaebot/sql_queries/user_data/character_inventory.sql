begin;

create table if not exists
    campaigns.character_inventory
(
    user_id bigint,
    campaign_id bigint,
    character_id int,
    item_id int,
    "name" text,
    "weight" text,
    created_time timestamp default now()
);

create index if not exists
    characters_inventory_idx
on
    campaigns.character_inventory(
        user_id,
        campaign_id,
        character_id
    )
;

commit;