<script lang="ts">
</script>

<svelte:head>
	<title>HayTracker Support | Code Pasture</title>
	<meta name="description" content="Get help with HayTracker, the simple hay inventory tracking app for iOS." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>HayTracker Support</h1>

		<section class="section">
			<h2>Contact Us</h2>
			<p>
				For questions, bug reports, or feature requests, please email us at:
			</p>
			<a href="mailto:haytracker@codepasture.com" class="email-link">haytracker@codepasture.com</a>
		</section>

		<section class="section">
			<h2>Frequently Asked Questions</h2>

			<div class="faq-item">
				<h3>How do I add a delivery?</h3>
				<p>Tap the "+" button on the Hay or Straw tab. Enter the bale type, number of bales, optional price per bale, delivery date, and any notes. The app will calculate total weight and cost automatically.</p>
			</div>

			<div class="faq-item">
				<h3>What's the difference between Stock, In Use, and Consumed?</h3>
				<p>For hay: bales start in <strong>Stock</strong>, move to <strong>In Use</strong> when deployed, then to <strong>Consumed</strong> when eaten. For straw: bales go directly from Stock to Consumed since there's no intermediate "in use" state.</p>
			</div>

			<div class="faq-item">
				<h3>How do I fix a mistake in my inventory count?</h3>
				<p>Use the adjustment feature to correct quantity mistakes. This creates a transaction record for your audit trail. Note that you cannot edit the bale type or count on existing deliveries to maintain accurate records.</p>
			</div>

			<div class="faq-item">
				<h3>Can I add custom bale types?</h3>
				<p>Yes. Go to More &rarr; Manage Bale Types to create custom types with your own dimensions and weights. Default bale types (like two-string, three-string, and round bales) are pre-loaded and cannot be deleted.</p>
			</div>

			<div class="faq-item">
				<h3>How do I export my data?</h3>
				<p>Go to More &rarr; Export/Import. You can export all data, just deliveries (useful for cost records), or just transactions (for usage history) as CSV files.</p>
			</div>

			<div class="faq-item">
				<h3>Where is my data stored?</h3>
				<p>All data is stored locally on your device. We do not collect or transmit any of your information. Your data is included in standard iCloud or iTunes device backups.</p>
			</div>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/haytracker/privacy">Privacy Policy</a>
			</p>
		</section>
	</main>
</div>

<style>
	.page {
		min-height: 100vh;
		padding: 2rem;
		max-width: 800px;
		margin: 0 auto;
	}

	.page-header {
		margin-bottom: 3rem;
	}

	.back-link {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	.back-link:hover {
		color: var(--color-accent);
	}

	.content h1 {
		font-size: 2rem;
		font-weight: 600;
		margin-bottom: 2rem;
	}

	.section {
		margin-bottom: 3rem;
	}

	.section h2 {
		font-size: 1.25rem;
		font-weight: 600;
		margin-bottom: 1rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.7;
	}

	.email-link {
		display: inline-block;
		margin-top: 0.5rem;
		font-size: 1.1rem;
		font-weight: 500;
	}

	.faq-item {
		margin-bottom: 1.5rem;
		padding: 1.25rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.faq-item h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.faq-item p {
		margin: 0;
		font-size: 0.95rem;
	}

	.footer-links {
		padding-top: 2rem;
		border-top: 1px solid var(--color-border);
	}

	@media (max-width: 768px) {
		.page {
			padding: 1.5rem;
		}

		.content h1 {
			font-size: 1.5rem;
		}
	}
</style>
