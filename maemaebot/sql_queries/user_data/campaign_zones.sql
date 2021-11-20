--table for zones

begin;

create table if not exists
    campaigns.campaign_zones
(
    server_id bigint,
    campaign_id bigint,
    channel_id bigint,
    page_url text,
    hostile text,
    created_time timestamp default now()
);

create index if not exists
    campaign_zones_id_idx
on
    campaigns.campaign_zones(
        server_id,
        campaign_id,
        channel_id
    )
;

commit;