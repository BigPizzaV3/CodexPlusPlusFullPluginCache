# Proxy selection guide

## Decision order

1. **Network identity requirement**
   - Consumer-network pool and rotation: start with Residential.
   - Stable consumer-ISP-classified address: start with ISP.
   - Carrier/mobile-network egress: start with Mobile.
   - Speed and static infrastructure address: start with Datacenter.
2. **Session behavior**
   - A long-lived login or workflow normally favors a dedicated static ISP or Datacenter endpoint.
   - Broad sampling normally favors rotating Residential.
   - A fixed identity within a pool may use a sticky session, subject to current limits.
3. **Location precision**
   - Confirm whether country is enough or whether city/region/ISP targeting is essential.
   - Never assume a specific location is currently in stock.
4. **Traffic and concurrency**
   - Estimate monthly GB, requests per minute, concurrent sessions, and the number of distinct identities.
   - A large traffic estimate alone does not determine proxy type; identity and session requirements come first.
5. **Protocol and client**
   - Confirm HTTP(S) versus SOCKS5 and whether the client actually supports proxy authentication and DNS handling.
   - Treat UDP support as an explicit compatibility requirement to verify, not as a default assumption.
6. **Sharing model**
   - Dedicated static endpoints prioritize consistency and isolation.
   - Pools prioritize breadth and rotation.

## Minimum questions

Ask these only if the answer is not already present:

1. What legitimate workflow will use the proxy?
2. Which countries or cities matter?
3. Do you need rotation, sticky sessions, or one static IP?
4. What monthly traffic and concurrent-session range do you expect?
5. Which application and protocol will connect?
6. Is a dedicated IP required?

## Recommendation patterns

- Localization QA across many countries: Residential, rotating or sticky according to test duration.
- Stable browser profile for permitted business operations: dedicated ISP; Datacenter as a lower-complexity alternative when ASN type is unimportant.
- High-throughput API or infrastructure task where datacenter IPs are accepted: Datacenter.
- Mobile-network application testing: Mobile.
- Mixed workflow: separate pools by function instead of forcing one proxy type to cover every job.

## Validation plan

Recommend a small controlled test before scaling:

1. Test the exact target geographies and application.
2. Measure connection success, latency, target response, session persistence, and effective cost per successful task.
3. Verify the visible IP, DNS behavior, WebRTC exposure, and intended session rotation.
4. Compare results across a representative time window rather than one request.
5. Confirm current terms and acceptable-use requirements before production use.
