# Fanbucks Backend Documentation

***

## User Registration

### Register a new user

**Endpoint:** `/api/auth/register/`

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

**Endpoint:** `/api/auth/login/`

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


### Log out an existing user

**Endpoint:** `/api/auth/logout/`

**Method:** `POST`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`

**Request Payload:** None

**Response:** None


## User Profile
### Retrieve user profile information
**Endpoint:** `/api/user/`

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
**Endpoint:** `/api/user/`

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


```



## Bucks

### Get all bucks for auth user
**Endpoint:** `/api/bucks/`

**Method:** `GET`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`

**Response:**

```json
[
    {
        "id": "b7df8094-f6c2-4b69-a4f7-daebfaa32caa",
        "title": "Buy new Macbook M1 Laptop",
        "description": "i want you guys to help me achieve my gool",
        "amount": 1000000,
        "status": "Pending",
        "owner": "14690570-06e5-4f21-b69d-ffa33accbd7f"
    },
    {
        "id": "e151e5f7-479e-42e9-8bf0-c5426bc36585",
        "title": "Buy new Macbook M1 Laptop",
        "description": "i want you guys to help me achieve my gool",
        "amount": 1000000,
        "status": "Pending",
        "owner": "14690570-06e5-4f21-b69d-ffa33accbd7f"
    }
]

```

## Create Bucks
**Endpoint:** `/api/bucks/`

**Method:** `POST`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`


**Request Payload:**

```json
{
  "title":"Buy new Macbook M1 Laptop",
  "description":"i want you guys to help me achieve my gool",
  "amount":"1000000.00"
}

```

**Response:**

```json
{
    "id": "e151e5f7-479e-42e9-8bf0-c5426bc36585",
    "title": "Buy new Macbook M1 Laptop",
    "description": "i want you guys to help me achieve my gool",
    "amount": "1000000.00",
    "status": "Pending",
    "owner": "14690570-06e5-4f21-b69d-ffa33accbd7f"
}
```

## Retrieve a Specific Buck
**Endpoint:** `/api/bucks/{uuid}/`

**Method:** `GET`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`

**Response:**

```json
{
    "id": "e151e5f7-479e-42e9-8bf0-c5426bc36585",
    "title": "Buy new Macbook M1 Laptop",
    "description": "i want you guys to help me achieve my gool",
    "amount": "1000000.00",
    "status": "Pending",
    "owner": "14690570-06e5-4f21-b69d-ffa33accbd7f"
}

```


## Update a specific Buck 
**Endpoint:** `/api/bucks/{uuid}/`

**Method:** `PUT/PATCH`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`


**Request Payload:**

```json
{
    "title": "Buy new Macbook M1 Laptop",
    "description": "i want you guys to help me achieve my gool",
    "amount": "1000000.00",
    "status": "Complete"
}

```




**Response:**

```json
{
    "id": "e151e5f7-479e-42e9-8bf0-c5426bc36585",
    "title": "Buy new Macbook M1 Laptop",
    "description": "i want you guys to help me achieve my gool",
    "amount": "1000000.00",
    "status": "Complete",
    "owner": "14690570-06e5-4f21-b69d-ffa33accbd7f"
}

```



## Delete a specific Buck 
**Endpoint:** `/api/bucks/{uuid}/`

**Method:** `DELETE`

**Authentication:** `Token-based (Include the obtained token in the Authorization header)`

