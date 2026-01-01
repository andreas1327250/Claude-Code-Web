# ÖBB Train Seat Availability App

A simple web application that shows train seat availability between Linz and Vienna using reverse-engineered ÖBB (Österreichische Bundesbahnen) public endpoints.

## Features

- 🚆 Real-time train connections between Linz and Vienna
- ⏰ Customizable departure date and time
- 💺 Seat availability information
- 📊 Train details including duration, platform, and pricing
- 🎨 Modern, responsive UI

## Reverse-Engineered ÖBB Endpoints

This app uses the public HAFAS (HaCon Fahrplan-Auskunfts-System) endpoints provided by ÖBB:

### 1. Station Search Endpoint

```
GET https://fahrplan.oebb.at/bin/ajax-getstop.exe/dn
```

**Parameters:**
- `getstop=1` - Enable station search
- `REQ0JourneyStopsS0A=1` - Return all matches
- `REQ0JourneyStopsS0G={query}` - Station name query

**Response Format:**
Tab-separated values with station name and ID:
```
Wien Hbf	8103000
Wien Meidling	8101073
...
```

### 2. Journey Query Endpoint

```
GET https://fahrplan.oebb.at/bin/query.exe/dn
```

**Parameters:**
- `S={from_station}` - Origin station name
- `Z={to_station}` - Destination station name
- `date={DD.MM.YY}` - Departure date
- `time={HH:MM}` - Departure time
- `start=1` - Search type (1 = departure)

**Response:** HTML page with journey connections

### 3. Station Board Endpoint

```
GET https://fahrplan.oebb.at/bin/stboard.exe/dn
```

Shows departures/arrivals for a specific station.

### 4. Live Train Map

```
GET http://zugradar.oebb.at/bin/help.exe/dn?tpl=livefahrplan
```

Displays all trains on a live map.

## API System: HAFAS

ÖBB uses the **HAFAS** (HaCon Fahrplan-Auskunfts-System) API, which is a journey planning system used by many European transportation providers. The same system is used by:

- Deutsche Bahn (Germany)
- SBB (Switzerland)
- NS (Netherlands)
- And many others

## How to Use

1. Open `index.html` in a web browser
2. Select your departure date and time (defaults to current time)
3. Click "Search Trains"
4. View available train connections with seat availability

## Technical Details

### CORS Proxy

Since the ÖBB endpoints don't support CORS (Cross-Origin Resource Sharing), the app uses a CORS proxy service (`allorigins.win`) to fetch data. For production use, consider:

1. Setting up your own backend proxy server
2. Using the official ÖBB API Portal (requires registration)
3. Running the app from a server that can make backend requests

### Mock Data

Currently, the app generates mock data for demonstration purposes because parsing the HTML response from ÖBB requires more sophisticated parsing. To implement real data:

1. Parse the HTML response from `query.exe/dn`
2. Or use existing libraries like:
   - [oebb-api](https://github.com/mymro/oebb-api) (Node.js)
   - [public-transport/oebb](https://github.com/juliuste/oebb) (Node.js)
   - [hafas-client](https://github.com/public-transport/hafas-client) (Generic HAFAS client)

### Alternative: Use Existing Libraries

For a production implementation, consider using existing open-source libraries:

```bash
# Node.js example with oebb-api
npm install oebb-api

# Usage
const oebb = require('oebb-api');

oebb.searchStationsNew("Linz Hbf").then((from) => {
    oebb.searchStationsNew("Wien Hbf").then((to) => {
        oebb.getJourneys(from[0], to[0], true).then(console.log);
    });
});
```

## Official ÖBB API

For production use, ÖBB provides an official API portal:

- **API Portal:** https://apiportal.oebb.at/portal/
- **InfoHub:** https://infohub.oebb.at/portal/

You need to register and request access to use official APIs.

## Resources

- [GitHub - mymro/oebb-api](https://github.com/mymro/oebb-api) - Node.js API wrapper
- [GitHub - public-transport/oebb](https://github.com/juliuste/oebb) - FPTI-compliant client
- [HAFAS Endpoints List](https://gist.github.com/marcus-at-localhost/fc051c429a53672e2389d328ce57074c)
- [ÖBB Official API Portal](https://apiportal.oebb.at/portal/)
- [ÖBB Open Data](https://www.data.gv.at/2020/01/10/offene-daten-oebb/)

## Disclaimer

This is an educational project demonstrating how to reverse-engineer public transportation APIs. For production use:

1. Use the official ÖBB API Portal
2. Request permission from ÖBB
3. Respect rate limits and terms of service
4. Consider data privacy and GDPR compliance

## License

This project is for educational purposes only. ÖBB and its data remain property of Österreichische Bundesbahnen.

## Contributing

Feel free to improve the HTML parsing, add more features, or enhance the UI!

## Future Enhancements

- [ ] Implement real HTML parsing for actual ÖBB data
- [ ] Add more station pairs
- [ ] Show platform changes
- [ ] Display train composition
- [ ] Add ticket booking links
- [ ] Implement real seat availability (requires official API)
- [ ] Add delay notifications
- [ ] Support for multiple routes
- [ ] Mobile app version
