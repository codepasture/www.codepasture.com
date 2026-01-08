<script lang="ts">
</script>

<svelte:head>
	<title>DevHours Support | Code Pasture</title>
	<meta name="description" content="Get help with DevHours, the simple time tracking app for iOS and Android." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>DevHours Support</h1>

		<section class="section">
			<h2>Contact Us</h2>
			<p>
				For questions, bug reports, or feature requests, please email us at:
			</p>
			<a href="mailto:devhours@codepasture.com" class="email-link">devhours@codepasture.com</a>
		</section>

		<section class="section">
			<h2>Frequently Asked Questions</h2>

			<div class="faq-item">
				<h3>How do I start tracking time?</h3>
				<p>Tap the play button to start a new time entry. You can assign it to a project and add a description. When you're done, tap stop to end the entry.</p>
			</div>

			<div class="faq-item">
				<h3>How do I create a new project?</h3>
				<p>Go to the Projects tab and tap the "+" button. Enter a project name and optional color to help organize your time entries.</p>
			</div>

			<div class="faq-item">
				<h3>Can I edit a time entry after it's saved?</h3>
				<p>Yes. Tap on any time entry to edit its start time, end time, project, description, or notes.</p>
			</div>

			<div class="faq-item">
				<h3>How do I export my time entries?</h3>
				<p>Use the export feature in the app settings to export your time entries as a CSV file. You can filter by date range or project before exporting.</p>
			</div>

			<div class="faq-item">
				<h3>Where is my data stored?</h3>
				<p>All data is stored locally on your device. We do not collect or transmit any of your information. Your data is included in standard device backups (iCloud or Google Drive).</p>
			</div>

			<div class="faq-item">
				<h3>Does the app work offline?</h3>
				<p>Yes. DevHours works entirely offline since all data is stored locally on your device. No internet connection is required.</p>
			</div>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/devhours/privacy">Privacy Policy</a>
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
