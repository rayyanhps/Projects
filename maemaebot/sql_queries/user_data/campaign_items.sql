-- table for campaign items, should include item damage and reach etc

begin;

create table if not exists
    campaigns.campaign_items
(
    campaign_id bigint,
    item_id int,
    item_name text,
    item_description text,
    item_weight int,
    item_attack text,
    item_attribute_id int,
    user_id bigint
)

create index if not exists
    items_id_idx
on
    campaigns.characters(
        campaign_id,
        item_id
    )
;