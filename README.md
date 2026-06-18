# Redis Cache Strategy

Redis caching strategies: write-through, cache-aside, read-through with stampede prevention.

## Strategies
- Cache-aside (lazy loading)
- Write-through (strong consistency)
- Write-behind (async, high throughput)
- Read-through (transparent)

## Features
- Stampede prevention (probabilistic early expiration)
- Multi-tier: L1 local + L2 Redis
- Cache warming on startup

## License: MIT
