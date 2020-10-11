# Documentations

- [follow](#follow)
  - [by_tags](#by_tags)
  - [by_locations](#by_locations)

## follow

| Option      | Type      | Description                                                                              |
| ----------- | --------- | ---------------------------------------------------------------------------------------- |
| enable      | boolean   | option allows you to enable or not the `follow` configuration                            |
| usernames   | list[str] | is a list of given instagram user names which your accounts will follow their followers. |
| amount      | int       | is the number of followers that you want to follow for each user names.                  |
| randomize   | boolean   | If is set to True, the bot will pick the `amount` of persons to follow randomly          |
| interact    | boolean   | Should to interact with the following account or not (like, comment)                     |
| sleep_delay | int       | Sleep delay before following the next account.                                           |
| by_tags     | object    | See [follow by tags](#by_tags)                                                           |

### by_tags

| Option                      | Type      | Description                                                                                                                                  |
| --------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| tags                        | list[str] | list of tags that you want to follow                                                                                                         |
| amount                      | int       | the number of users that you want to follow by tags                                                                                          |
| randomize                   | boolean   | If is set to True, the bot will pick the `amount` of persons to follow randomly                                                              |
| interact                    | boolean   | Should to interact with the following account or not (like, comment)                                                                         |
| media                       | str       | Follow Photo or Video media. Possible values are `Photo` and `Video`. If media is not deinfed in config, the bot will follow both by default |
| skip_top_posts              | bool      | Will ignore the 9 first posts for each hashtags                                                                                              |
| use_smart_hashtags          | bool      | Smart hashtags feature                                                                                                                       |
| use_smart_location_hashtags | bool      | Smart location hashtags feature                                                                                                              |

### by_locations

| Option         | Type      | Description                                                                                                                                  |
| -------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| locations      | list[str] | list of locations that you want to follow people                                                                                             |
| amount         | int       | is the number of followers that you want to follow for each user names.                                                                      |
| media          | str       | Follow Photo or Video media. Possible values are `Photo` and `Video`. If media is not deinfed in config, the bot will follow both by default |
| skip_top_posts | bool      | Will ignore the 9 first posts for each hashtags                                                                                              |
