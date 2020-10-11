# Documentations

- [follow](#follow)

## follow

| Option      | Type      | Description                                                                              |
| ----------- | --------- | ---------------------------------------------------------------------------------------- |
| enable      | boolean   | option allows you to enable or not the `follow` configuration                            |
| usernames   | list[str] | is a list of given instagram user names which your accounts will follow their followers. |
| amount      | int       | is the number of followers that you want to follow for each user names.                  |
| randomize   | boolean   | If is set to True, the bot will pick the `amount` of persons to follow randomly          |
| interact    | boolean   | Should to interact with the following account or not (like, comment)                     |
| sleep_delay | int       | Sleep delay before following the next account.                                           |
