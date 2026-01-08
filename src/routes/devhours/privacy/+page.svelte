<script lang="ts">
</script>

<svelte:head>
	<title>DevHours Privacy Policy | Code Pasture</title>
	<meta name="description" content="Privacy policy for DevHours, the time tracking app for iOS and Android." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>DevHours Privacy Policy</h1>
		<p class="effective-date">Effective Date: December 5, 2025</p>

		<section class="section">
			<h2>Overview</h2>
			<p>
				DevHours is designed with your privacy in mind. We do not collect, store, or transmit any personal information or usage data. All information you enter stays on your device.
			</p>
		</section>

		<section class="section">
			<h2>Data Storage</h2>
			<p>
				All data you enter into DevHours is stored locally on your device using a SQLite database. Your time entries, projects, work items, and notes never leave your device and are not accessible to us or any third parties.
			</p>
		</section>

		<section class="section">
			<h2>Data Collection</h2>
			<p>
				DevHours does not collect any data. Specifically:
			</p>
			<ul>
				<li>No personal information is collected</li>
				<li>No usage analytics or tracking</li>
				<li>No location data</li>
				<li>No device identifiers</li>
				<li>No crash reports or telemetry</li>
				<li>No third-party analytics services</li>
			</ul>
		</section>

		<section class="section">
			<h2>Third-Party Services</h2>
			<p>
				DevHours does not integrate with any third-party services, analytics platforms, or advertising networks that collect user data. The app functions entirely offline and does not require an internet connection.
			</p>
		</section>

		<section class="section">
			<h2>Data Export</h2>
			<p>
				The app provides functionality to export your time entries. When you use this feature, you control what happens with the exported data. We have no involvement in or access to your exported data.
			</p>
		</section>

		<section class="section">
			<h2>Data Backup</h2>
			<p>
				Your DevHours data may be included in your device's standard backup process (iCloud, Google Drive, or local backups). These backups are managed by Apple or Google and are subject to their respective privacy policies.
			</p>
		</section>

		<section class="section">
			<h2>Data Retention and Deletion</h2>
			<p>
				Your data remains on your device until you choose to delete it. You can delete individual time entries within the app or uninstall the app to remove all associated data. We have no ability to access, retain, or delete your data as it exists only on your device.
			</p>
		</section>

		<section class="section">
			<h2>Children's Privacy</h2>
			<p>
				DevHours does not collect any information from anyone, including children under the age of 13.
			</p>
		</section>

		<section class="section">
			<h2>Changes to This Policy</h2>
			<p>
				We may update this privacy policy from time to time. Any changes will be posted on this page with an updated effective date. Significant changes will be noted in the app's update notes on the App Store and Google Play Store.
			</p>
		</section>

		<section class="section">
			<h2>Contact</h2>
			<p>
				If you have any questions about this privacy policy, please contact us at:
			</p>
			<a href="mailto:devhours@codepasture.com" class="email-link">devhours@codepasture.com</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/devhours/support">Support</a>
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
		margin-bottom: 0.5rem;
	}

	.effective-date {
		color: var(--color-text-muted);
		font-size: 0.9rem;
		margin-bottom: 2rem;
	}

	.section {
		margin-bottom: 2rem;
	}

	.section h2 {
		font-size: 1.25rem;
		font-weight: 600;
		margin-bottom: 0.75rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.7;
	}

	.section ul {
		color: var(--color-text-muted);
		line-height: 1.8;
		padding-left: 1.5rem;
		margin-top: 0.5rem;
	}

	.section li {
		margin-bottom: 0.25rem;
	}

	.email-link {
		display: inline-block;
		margin-top: 0.5rem;
		font-size: 1.1rem;
		font-weight: 500;
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
