## What the hell is this?

### This is a simple demonstration of security implementation without oauth and similar approaches.

## Why?

### I believe that using tokens (oauth) is complex and might be not surefire. In the meantime, using a permanenet api key (update it only when a user forgets password) and refreshing api calls for this key every N days/hours/minutes is more convenient, because there is no need to pass new access token in response in every backend handler and update this token somewhere on client-side too. It would be easier to have a single api key for a user, but if a user gets hacked or his/her api key is leaked, a user can refresh his password.
