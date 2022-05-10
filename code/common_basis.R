library(tidyverse)
library(DBI)
library(keyring)
library(RMariaDB)
library(pool)

if (!("convoy" %in% key_list("convoy"))) key_set("convoy", "convoy")

con <- tryCatch(
  dbPool(
    drv = MariaDB(),
    host = "vm1788.kaj.pouta.csc.fi",
    dbname = "convoy",
    user = "convoy",
    password = key_get("convoy", "convoy"),
    bigint = "numeric",
    load_data_local_infile = T,
    validationInterval = 10
  ),
  error = function(e) {
    key_delete("convoy", "convoy")
    stop(e)
  }
)
dbExecute(con, "SET SESSION storage_engine=aria")
con_i <- dbPool(drv = MariaDB(), host = "vm1788.kaj.pouta.csc.fi", dbname = "convoy", user = "convoy", password = key_get("convoy", "convoy"), bigint = "integer64", load_data_local_infile = T, validationInterval = 10)
dbExecute(con_i, "SET SESSION storage_engine=aria")

tweets_c <- tbl(con, "tweets_c")
tweets_a <- tbl(con, "tweets_a")
users_c <- tbl(con, "users_c")
users_a <- tbl(con, "users_a")
tweet_hashtags_c <- tbl(con, "tweet_hashtags_c")
tweet_hashtags_a <- tbl(con, "tweet_hashtags_a")
tweet_mentions_c <- tbl(con, "tweet_mentions_c")
tweet_mentions_a <- tbl(con, "tweet_mentions_a")
tweet_urls_c <- tbl(con, "tweet_urls_c")
tweet_urls_a <- tbl(con, "tweet_urls_a")
conversations_c <- tbl(con, "conversations_c")
conversations_a <- tbl(con, "conversations_a")
ur_conversations_c <- tbl(con, "ur_conversations_c")
ur_conversations_a <- tbl(con, "ur_conversations_a")

tweets_c_i <- tbl(con_i, "tweets_c")
tweets_a_i <- tbl(con_i, "tweets_a")
users_c_i <- tbl(con_i, "users_c")
users_a_i <- tbl(con_i, "users_a")
tweet_hashtags_c_i <- tbl(con_i, "tweet_hashtags_c")
tweet_hashtags_a_i <- tbl(con_i, "tweet_hashtags_a")
tweet_mentions_c_i <- tbl(con_i, "tweet_mentions_c")
tweet_mentions_a_i <- tbl(con_i, "tweet_mentions_a")
tweet_urls_c_i <- tbl(con_i, "tweet_urls_c")
tweet_urls_a_i <- tbl(con_i, "tweet_urls_a")
conversations_c_i <- tbl(con_i, "conversations_c")
conversations_a_i <- tbl(con_i, "conversations_a")
ur_conversations_c_i <- tbl(con_i, "ur_conversations_c")
ur_conversations_a_i <- tbl(con_i, "ur_conversations_a")
