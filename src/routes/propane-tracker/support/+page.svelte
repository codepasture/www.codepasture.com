<script lang="ts">
</script>

<svelte:head>
	<title>Propane Tracker Support | Code Pasture</title>
	<meta name="description" content="Get help with Propane Tracker, the simple propane tank monitoring app for iOS." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>Propane Tracker Support</h1>

		<section class="section">
			<h2>Contact Us</h2>
			<p>
				For questions, bug reports, or feature requests, please email us at:
			</p>
			<a href="mailto:propane-tracker@codepasture.com" class="email-link">propane-tracker@codepasture.com</a>
		</section>

		<section class="section">
			<h2>Frequently Asked Questions</h2>

			<div class="faq-item">
				<h3>How do I get started?</h3>
				<p>When you first open the app, you'll be asked to set up your tank by selecting its capacity (common sizes like 120, 250, 500, or 1000 gallons are pre-populated, or enter a custom size). You can optionally add a location label. After setup, you're ready to start logging readings.</p>
			</div>

			<div class="faq-item">
				<h3>How do I add a tank reading?</h3>
				<p>Tap "Add Reading" on the dashboard. Enter the percentage shown on your tank gauge (0-100%). You can use the quick buttons for common levels (10%, 25%, 50%, 75%, 100%). Optionally add the date, temperature, and notes.</p>
			</div>

			<div class="faq-item">
				<h3>How do I log a delivery?</h3>
				<p>Tap "Add Delivery" on the dashboard. Enter the delivery date, gallons delivered, and total cost. The app automatically calculates your price per gallon. You can optionally record the tank level before and after delivery for more accurate consumption tracking.</p>
			</div>

			<div class="faq-item">
				<h3>What do the tank colors mean?</h3>
				<p><strong>Green</strong> means your tank is above 35%. <strong>Orange</strong> means you're between 20-35%. <strong>Red</strong> means you're below 20% and should consider scheduling a delivery.</p>
			</div>

			<div class="faq-item">
				<h3>How is consumption calculated?</h3>
				<p>The app calculates consumption two ways: percentage per day (from your gauge readings) and gallons per day (from deliveries). It uses a 90-day rolling window and estimates how many days until your tank reaches 20%.</p>
			</div>

			<div class="faq-item">
				<h3>Can I edit or delete entries?</h3>
				<p>Yes. Go to Reading History or Delivery History, tap an entry, and you can edit or delete it. All changes are saved with timestamps for your records.</p>
			</div>

			<div class="faq-item">
				<h3>How do I export my data?</h3>
				<p>Go to Settings &rarr; Export Data. Your readings, deliveries, and tank configuration are exported as CSV files that you can open in any spreadsheet application.</p>
			</div>

			<div class="faq-item">
				<h3>Where is my data stored?</h3>
				<p>All data is stored locally on your device. We do not collect or transmit any of your information. Your data is included in standard iCloud or iTunes device backups.</p>
			</div>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/propane-tracker/privacy">Privacy Policy</a>
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
