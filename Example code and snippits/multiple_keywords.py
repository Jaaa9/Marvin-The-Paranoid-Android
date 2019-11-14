=== CODE SNIPPITS == 

#To make the bot check for multiple key words, you can use an array of aliases like this: 
import random
@client.command(aliases=['Quote', '!Quote', 'quote', 'Time for a quote']
async def quotes(ctx,*, quotes):
	respons =['Quotes.', 'Quotes.', 'Quotes.', 'Quotes.', 'Quotes.', ]
		await ctx.send(f'Quote: {quotes}\nAnswer: {random.choice(respons)}') 
