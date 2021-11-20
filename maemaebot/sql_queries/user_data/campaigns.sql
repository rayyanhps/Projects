begin;

create table if not exists
    campaigns.campaigns
(
    user_id bigint,
    server_id bigint,
    campaign_id int,
    page_url text,
    modifier int,
    whitelist boolean,
    public boolean,
    created_time timestamp default now()
);

create index if not exists
    campaigns_user_id_idx
on
    campaigns.campaigns(
        user_id,
        server_id,
        campaign_id
    )
;

commit;