# Documentations

- [follow](#follow)
  - [by_tags](#by_tags)
  - [by_locations](#by_locations)
- [unfollow](#unfollow)
- [like_by_feed](#like_by_feed)

## follow

| Option       | Type      | Description                                                                              | Values        | Default value |
| ------------ | --------- | ---------------------------------------------------------------------------------------- | ------------- | ------------- |
| enable       | boolean   | option allows you to enable or not the `follow` configuration                            | true \| false | false         |
| usernames    | list[str] | is a list of given instagram user names which your accounts will follow their followers. | []            | []            |
| amount       | int       | is the number of followers that you want to follow for each user names.                  |               | 250           |
| randomize    | boolean   | If is set to True, the bot will pick the `amount` of persons to follow randomly          | true \| false | true          |
| interact     | boolean   | Should to interact with the following account or not (like, comment)                     | true \| false | false         |
| sleep_delay  | int       | Sleep delay before following the next account.                                           |               | 600           |
| by_tags      | object    | See [follow by tags](#by_tags)                                                           | {}            | None          |
| by_locations | object    | See [follow by locations](#by_locations)                                                 | {}            | None          |

### by_tags

| Option                      | Type      | Description                                                                                                                                  | Values         | Default value |
| --------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------- |
| tags                        | list[str] | list of tags that you want to follow                                                                                                         | []             | []            |
| amount                      | int       | the number of users that you want to follow by tags                                                                                          |                | 0             |
| randomize                   | boolean   | If is set to True, the bot will pick the `amount` of persons to follow randomly                                                              | true \| false  | true          |
| interact                    | boolean   | Should to interact with the following account or not (like, comment)                                                                         | true \| false  | false         |
| media                       | str       | Follow Photo or Video media. Possible values are `Photo` and `Video`. If media is not deinfed in config, the bot will follow both by default | Photo \| Video | None          |
| skip_top_posts              | bool      | Will ignore the 9 first posts for each hashtags                                                                                              | true \| false  | false         |
| use_smart_hashtags          | bool      | Smart hashtags feature                                                                                                                       | true \| false  | false         |
| use_smart_location_hashtags | bool      | Smart location hashtags feature                                                                                                              | true \| false  | false         |

### by_locations

| Option         | Type      | Description                                                                                                                                  | Values         | Default value |
| -------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------- |
| locations      | list[str] | list of locations that you want to follow people                                                                                             | []             | []            |
| amount         | int       | is the number of followers that you want to follow for each user names.                                                                      |                | 0             |
| media          | str       | Follow Photo or Video media. Possible values are `Photo` and `Video`. If media is not deinfed in config, the bot will follow both by default | Photo \| Video | None          |
| skip_top_posts | bool      | Will ignore the 9 first posts for each hashtags                                                                                              | true \| false  | true          |

## unfollow

| Option                 | Type | Description                                                                                                      | Values                 | Default value |
| ---------------------- | ---- | ---------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------- |
| enable                 | bool | Enable unfollow feature                                                                                          | true \| false          | false         |
| amount                 | int  | is the number of users that you want to unfollow for each user names.                                            |                        | 0             |
| non_followers          | bool | When this option is set to true. Floflow will only unfollow users that are that following you back.              | true \| false          | false         |
| all_following          | bool | When this option is set to true. Floflow will unfollow every users, except users which are in your white list    | true \| false          | false         |
| white_list             | list | List of users that you don't want to unfollow                                                                    | []                     | []            |
| sleep_delay            | int  | Sleep delay before following the next account.                                                                   |                        | 600           |
| custom_list_enabled    | bool | Enable custom list option, this option will unfollow your custom list only. Except your white list               | true \| false          | false         |
| custom_list            | list | The custom list that you want to unfollow                                                                        | []                     | []            |
| custom_list_param      | str  | "all" value for unfollow all those users, and "nonfollowers" will unfollow users that are not following you back | all \| nonfollowers    | all           |
| instapy_list_enabled   | bool | Enable instapy custom option will unfollow users are only followed by Instapy before                             | true \| false          | false         |
| instapy_followed_param | str  | Same as `custom_list_param`                                                                                      | all \| nonfollowers    | all           |
| style                  | str  | The style that you wan to unfollow                                                                               | FIFO \| LIFO \| RANDOM | RANDOM        |
| unfollow_after         | int  | Unfollow after X minutes or hours                                                                                |                        | None          |

## like_by_feed
| Option         | Type      | Description                                                                                                                                  | Values         | Default value |
| -------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------- |
| amount         | int       | is the number of followers that you want to like in your feed.                                                                               |                | 100           |
| randomize      | boolean   | If is set to True, the bot will pick the `amount` of posts to like randomly                                                                  | true \| false  | true          |
| interact       | boolean   | Should to interact with user  account or not (like)                                                                                          | true \| false  | true          |
| unfollow       | boolean   | Unfollows the author of a post which was considered inappropriate                                                                            | true \| false  | true          |
