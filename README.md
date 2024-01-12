# Fanbucks Backend Documentation

***

## User Registration

### Register a new user

**Endpoint:** `/register/`

**Method:** `POST`

**Authentication:** None

**Request Payload:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "username": "test@email.com",
  "password": "securepassword123"
}
```

**Response:**

```json
{
  "id": 1,
  "username": "test@email.com",
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe",
  "profile_pic": null,
  "birth_date": null,
  "address": null,
  "phone_number": null,
  "job_role": null,
  "portfolio_link": null,
  "country": null,
  "bio": ""
}

```

## User Authentication

### Log in an existing user

**Endpoint:** `/login/`

**Method:** `POST`

**Authentication:** None

**Request Payload:**

```json
{
  
  "username": "test@email.com",
  "password": "securepassword123"

}
```

**Response:**

```json
{
  "token": "your-auth-token"
}

```


## User Profile
### Retrieve user profile information
**Endpoint:** `/user/`

**Method:** `GET`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`

**Response:**

```json
{
  "id": 1,
  "username": "johndoe",
  "first_name": "John",
  "last_name": "Doe",
  "email": "test@email.com",
  "profile_pic": null,
  "birth_date": null,
  "address": null,
  "phone_number": null,
  "job_role": null,
  "portfolio_link": null,
  "country": null,
  "bio": ""
}

```

### Update user profile information
**Endpoint:** `/user/`

**Method:** `PUT`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`

**Request Payload:**

```json
{
  "first_name": "UpdatedFirstName",
  "last_name": "UpdatedLastName",
  "profile_pic": "updated_profile_pic.jpg",
  "birth_date": "1990-01-01",
  "address": "123 Updated Street",
  "phone_number": "555-555-5555",
  "job_role": "Updated Job Role",
  "portfolio_link": "http://updated-portfolio.com",
  "country": "Updated Country",
  "bio": "Updated user bio."
}

```

**Response:**

```json
{
  "id": 1,
  "username": "johndoe",
  "first_name": "UpdatedFirstName",
  "last_name": "UpdatedLastName",
  "email": "johndoe",
  "profile_pic": "updated_profile_pic.jpg",
  "birth_date": "1990-01-01",
  "address": "123 Updated Street",
  "phone_number": "555-555-5555",
  "job_role": "Updated Job Role",
  "portfolio_link": "http://updated-portfolio.com",
  "country": "Updated Country",
  "bio": "Updated user bio."
}

}

```