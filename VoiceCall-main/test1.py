import plivo

auth_id = 'MAMJDKMDVJODI2ZTK3MG'
auth_token = 'ZGQyODQ1OTVmODA3ODAyYTFmNjFmODBjOTY5NThm'
phlo_id = 'e0d92b9a-3e5e-4eb1-b9ab-17de1f4ece86'
phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
phlo = phlo_client.phlo.get(phlo_id)
response = phlo.run()
print(response)    

