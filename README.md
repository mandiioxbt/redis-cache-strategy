# Redis Cache Strategy

Redis caching strategies: write-through, cache-aside, read-through.

## Strategies
- Cache-aside (lazy loading)
- Write-through (consistent)
- Write-behind (async)
- Read-through (transparent)

## Features
- Cache warming
- Stampede prevention (probabilistic early expiration)
- Multi-tier caching (L1 local + L2 Redis)

## License
MIT
